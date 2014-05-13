from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, RedirectView
from youtube_rss_proxy.models import Rss
from youtube_rss_proxy.utils import get_auth_url, get_tokens, refresh_token, get_rss, get_username, InvalidToken
from uuid import uuid1


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
            obj.delete()
        else:
            if not obj.access_token:
                access_token, refresh_token = get_tokens(self.request.GET["code"])
                obj.access_token = access_token
                obj.refresh_token = refresh_token
                obj.save()
            if not obj.username:
                try:
                    obj.username = get_username(obj.access_token)
                except InvalidToken:
                    if obj.refresh_token:
                        obj.access_token = refresh_token(obj.refresh_token)
                        obj.save()
                        try:
                            obj.username = get_username(obj.access_token)
                        except InvalidToken:
                            context = {"error": True}
                            obj.delete()
                else:
                    obj.save()
            context = {
                "url": self.request.build_absolute_uri(reverse("rss-proxy", kwargs={"uuid": obj.uuid})),
            }
        context.update(kwargs)
        return context


def rss_proxy(request, uuid):
    obj = get_object_or_404(Rss, uuid=uuid)
    if not obj.access_token:
        obj.delete()
        raise Http404
    try:
        rss, content_type = get_rss(obj.username, obj.access_token)
    except InvalidToken:
        if obj.refresh_token:
            try:
                obj.access_token = refresh_token(obj.refresh_token)
            except InvalidToken:
                obj.delete()
                raise Http404
            obj.save()
            try:
                rss, content_type = get_rss(obj.username, obj.access_token)
            except InvalidToken:
                obj.delete()
                raise Http404
        else:
            obj.delete()
            raise Http404

    return HttpResponse(rss, content_type=content_type)
