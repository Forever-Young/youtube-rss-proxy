from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from youtube_rss_proxy.views import HomeView, OAuthCallbackView, rss_proxy, AuthRedirectView


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^auth$', csrf_exempt(AuthRedirectView.as_view()), name='auth_redirect'),
    url(r'^oauth2callback$', OAuthCallbackView.as_view(), name='oauth-callback'),
    url(r'^rss/(?P<uuid>[^/]+)/$', rss_proxy, name='rss-proxy'),

    url(r'^admin/', include(admin.site.urls)),
)
