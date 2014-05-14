from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from youtube_rss_proxy.views import HomeView, OAuthCallbackView, AuthRedirectView, rss_proxy_by_uuid, \
    rss_proxy_by_username


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^auth$', csrf_exempt(AuthRedirectView.as_view()), name='auth_redirect'),
    url(r'^oauth2callback$', OAuthCallbackView.as_view(), name='oauth-callback'),
    url(r'^rss/(?P<uuid>[^/]+)/$', rss_proxy_by_uuid, name='rss-proxy-by-uuid'),
    url(r'^user/(?P<username>[^/]+)/$', rss_proxy_by_username, name='rss-proxy-by-username'),

    url(r'^admin/', include(admin.site.urls)),
)
