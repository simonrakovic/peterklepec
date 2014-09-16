# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'novice.img'
        db.delete_column(u'webpage_novice', 'img')


    def backwards(self, orm):
        # Adding field 'novice.img'
        db.add_column(u'webpage_novice', 'img',
                      self.gf('django.db.models.fields.files.ImageField')(default='null', max_length=100),
                      keep_default=False)


    models = {
        u'webpage.novice': {
            'Meta': {'object_name': 'novice'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['webpage']