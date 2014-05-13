# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Rss.created_at'
        db.add_column('youtube_rss_proxy_rss', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Rss.created_at'
        db.delete_column('youtube_rss_proxy_rss', 'created_at')


    models = {
        'youtube_rss_proxy.rss': {
            'Meta': {'object_name': 'Rss'},
            'access_token': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'refresh_token': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36'})
        }
    }

    complete_apps = ['youtube_rss_proxy']