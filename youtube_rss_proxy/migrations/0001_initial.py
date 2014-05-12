# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Rss'
        db.create_table('youtube_rss_proxy_rss', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('access_token', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('refresh_token', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36)),
        ))
        db.send_create_signal('youtube_rss_proxy', ['Rss'])


    def backwards(self, orm):
        # Deleting model 'Rss'
        db.delete_table('youtube_rss_proxy_rss')


    models = {
        'youtube_rss_proxy.rss': {
            'Meta': {'object_name': 'Rss'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'refresh_token': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36'})
        }
    }

    complete_apps = ['youtube_rss_proxy']