from django.contrib import admin
from .models import Rss, Settings


class RssAdmin(admin.ModelAdmin):
    search_fields = ('uuid',)
    list_display = ('username', 'uuid', 'access_count', 'last_access')
    list_filter = ('username',)

admin.site.register(Rss, RssAdmin)
admin.site.register(Settings)
