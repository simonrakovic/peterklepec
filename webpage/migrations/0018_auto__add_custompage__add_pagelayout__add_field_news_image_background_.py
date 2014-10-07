# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CustomPage'
        db.create_table(u'webpage_custompage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')()),
            ('pageLayoutID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webpage.PageLayout'])),
        ))
        db.send_create_signal(u'webpage', ['CustomPage'])

        # Adding model 'PageLayout'
        db.create_table(u'webpage_pagelayout', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('template_path', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'webpage', ['PageLayout'])

        # Adding field 'News.image_background'
        db.add_column(u'webpage_news', 'image_background',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['webpage.Images']),
                      keep_default=False)

        # Adding field 'News.page_link'
        db.add_column(u'webpage_news', 'page_link',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['webpage.CustomPage'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'CustomPage'
        db.delete_table(u'webpage_custompage')

        # Deleting model 'PageLayout'
        db.delete_table(u'webpage_pagelayout')

        # Deleting field 'News.image_background'
        db.delete_column(u'webpage_news', 'image_background_id')

        # Deleting field 'News.page_link'
        db.delete_column(u'webpage_news', 'page_link_id')


    models = {
        u'webpage.customertype': {
            'Meta': {'object_name': 'CustomerType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'webpage.custompage': {
            'Meta': {'object_name': 'CustomPage'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pageLayoutID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webpage.PageLayout']"})
        },
        u'webpage.exercises': {
            'Meta': {'object_name': 'Exercises'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'exercises_page_layout': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['webpage.ExercisesPageLayout']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'position_number_on_main_page': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'show_on_main_page': ('django.db.models.fields.BooleanField', [], {}),
            'show_on_pricelist': ('django.db.models.fields.BooleanField', [], {}),
            'show_on_timetable': ('django.db.models.fields.BooleanField', [], {})
        },
        u'webpage.exercisespagelayout': {
            'Meta': {'object_name': 'ExercisesPageLayout'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'webpage.exercisesweeklytimetable': {
            'Meta': {'object_name': 'ExercisesWeeklyTimetable'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'exercisesID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webpage.Exercises']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timeFrom': ('django.db.models.fields.TimeField', [], {}),
            'timeTo': ('django.db.models.fields.TimeField', [], {}),
            'weekDay': ('django.db.models.fields.IntegerField', [], {})
        },
        u'webpage.imageplacement': {
            'Meta': {'object_name': 'ImagePlacement'},
            'description': ('django.db.models.fields.TextField', [], {'default': 'None'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'webpage.images': {
            'Meta': {'object_name': 'Images'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'exercisesID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webpage.Exercises']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageDestination': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'imagePlacementID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webpage.ImagePlacement']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'webpage.news': {
            'Meta': {'object_name': 'News'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_background': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webpage.Images']"}),
            'page_link': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['webpage.CustomPage']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'webpage.notworkinghours': {
            'Meta': {'object_name': 'NotWorkingHours'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'exercisesID': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['webpage.Exercises']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timeFrom': ('django.db.models.fields.TimeField', [], {}),
            'timeTo': ('django.db.models.fields.TimeField', [], {}),
            'weekDay': ('django.db.models.fields.IntegerField', [], {})
        },
        u'webpage.pagelayout': {
            'Meta': {'object_name': 'PageLayout'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'template_path': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'webpage.prices': {
            'Meta': {'object_name': 'Prices'},
            'customerTypeID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webpage.CustomerType']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'priceUnit': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'pricingPlanID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webpage.PricingPlan']"})
        },
        u'webpage.pricingplan': {
            'Meta': {'object_name': 'PricingPlan'},
            'exercisesID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webpage.Exercises']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['webpage']