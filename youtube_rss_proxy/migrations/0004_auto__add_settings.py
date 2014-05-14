# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Settings'
        db.create_table('youtube_rss_proxy_settings', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('access_token', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=255)),
            ('refresh_token', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=255)),
            ('last_access', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('access_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('youtube_rss_proxy', ['Settings'])


    def backwards(self, orm):
        # Deleting model 'Settings'
        db.delete_table('youtube_rss_proxy_settings')


    models = {
        'youtube_rss_proxy.rss': {
            'Meta': {'object_name': 'Rss'},
            'access_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'access_token': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '255'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_access': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'refresh_token': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '255'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36'})
        },
        'youtube_rss_proxy.settings': {
            'Meta': {'object_name': 'Settings'},
            'access_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'access_token': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_access': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'refresh_token': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['youtube_rss_proxy']