# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'novice'
        db.create_table(u'webpage_novice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('naslov', self.gf('django.db.models.fields.TextField')()),
            ('vsebina', self.gf('django.db.models.fields.TextField')()),
            ('slika', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'webpage', ['novice'])


    def backwards(self, orm):
        # Deleting model 'novice'
        db.delete_table(u'webpage_novice')


    models = {
        u'webpage.novice': {
            'Meta': {'object_name': 'novice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naslov': ('django.db.models.fields.TextField', [], {}),
            'slika': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'vsebina': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['webpage']