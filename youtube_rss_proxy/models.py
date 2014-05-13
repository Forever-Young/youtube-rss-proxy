from django.db import models


class Rss(models.Model):
    access_token = models.CharField(verbose_name="Access Token", max_length=255, blank=True, null=True)
    refresh_token = models.CharField(verbose_name="Refresh Token", max_length=255, blank=True, null=True)
    username = models.CharField(verbose_name="User name", max_length=255, blank=True, null=True)
    uuid = models.CharField(verbose_name="UUID", max_length=36)
    created_at = models.DateTimeField(verbose_name="Created", auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.username)


    class Meta:
        verbose_name = "RSS user feed"
        verbose_name_plural = "RSS user feeds"
