from uuid import uuid1
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, RedirectView

from .models import Rss, Settings
from .utils import get_auth_url, get_tokens, refresh_token, get_rss, get_username, InvalidToken


class HomeView(TemplateView):
    template_name = "home.html"


class AuthRedirectView(RedirectView):
    def get_redirect_url(self):
        obj = Rss.objects.create(
            uuid=str(uuid1()),
        )
        return get_auth_url(obj.uuid)


class OAuthCallbackView(TemplateView):
    template_name = "result.html"

    def get_context_data(self, **kwargs):
        obj = get_object_or_404(Rss, uuid=self.request.GET["state"])
        if self.request.GET.get("error") == "access_denied":
            context = {"error": True}
        else:
            obj.access_token, obj.refresh_token = get_tokens(self.request.GET["code"])
            obj.username = get_username(obj.access_token)
            obj.save()
            context = {
                "url": self.request.build_absolute_uri(reverse("rss-proxy-by-uuid", kwargs={"uuid": obj.uuid})),
            }
        context.update(kwargs)
        return context


def rss_proxy(request, obj, username='default'):
    if not obj.access_token and not obj.refresh_token:
        raise Http404
    try:
        rss, content_type = get_rss(obj.access_token, request.META["QUERY_STRING"], username)
    except InvalidToken:
        if obj.refresh_token:
            try:
                obj.access_token = refresh_token(obj.refresh_token)
            except InvalidToken:
                raise Http404
            obj.save()
            try:
                rss, content_type = get_rss(obj.access_token, request.META["QUERY_STRING"], username)
            except InvalidToken:
                raise Http404
        else:
            raise Http404

    obj.access_count = obj.access_count + 1
    obj.last_access = datetime.now()
    obj.save()
    return HttpResponse(rss, content_type=content_type)


def rss_proxy_by_uuid(request, uuid):
    obj = get_object_or_404(Rss, uuid=uuid)
    return rss_proxy(request, obj)


def rss_proxy_by_username(request, username):
    obj = Settings.objects.all()[0]
    return rss_proxy(request, obj, username)
