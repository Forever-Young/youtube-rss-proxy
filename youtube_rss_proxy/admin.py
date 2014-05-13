from django.contrib import admin
from .models import Rss
from . import filters


class RssAdmin(admin.ModelAdmin):
    search_fields = ('uuid',)
    list_display = ('username', 'uuid', 'access_count', 'last_access')
    list_filter = ('username',)

admin.site.register(Rss, RssAdmin)
