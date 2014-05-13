# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Rss.last_access'
        db.add_column('youtube_rss_proxy_rss', 'last_access',
                      self.gf('django.db.models.fields.DateTimeField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'Rss.access_count'
        db.add_column('youtube_rss_proxy_rss', 'access_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Rss.last_access'
        db.delete_column('youtube_rss_proxy_rss', 'last_access')

        # Deleting field 'Rss.access_count'
        db.delete_column('youtube_rss_proxy_rss', 'access_count')


    models = {
        'youtube_rss_proxy.rss': {
            'Meta': {'object_name': 'Rss'},
            'access_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'access_token': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_access': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'refresh_token': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36'})
        }
    }

    complete_apps = ['youtube_rss_proxy']