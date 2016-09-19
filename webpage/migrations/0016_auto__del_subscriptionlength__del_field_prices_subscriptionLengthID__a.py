# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'SubscriptionLength'
        db.delete_table(u'webpage_subscriptionlength')

        # Deleting field 'Prices.subscriptionLengthID'
        db.delete_column(u'webpage_prices', 'subscriptionLengthID_id')

        # Adding field 'Prices.description'
        db.add_column(u'webpage_prices', 'description',
                      self.gf('django.db.models.fields.TextField')(default=None),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'SubscriptionLength'
        db.create_table(u'webpage_subscriptionlength', (
            ('lengthNumber', self.gf('django.db.models.fields.IntegerField')()),
            ('lengthUnit', self.gf('django.db.models.fields.CharField')(max_length=20)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'webpage', ['SubscriptionLength'])

        # Adding field 'Prices.subscriptionLengthID'
        db.add_column(u'webpage_prices', 'subscriptionLengthID',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['webpage.SubscriptionLength']),
                      keep_default=False)

        # Deleting field 'Prices.description'
        db.delete_column(u'webpage_prices', 'description')


    models = {
        u'webpage.customertype': {
            'Meta': {'object_name': 'CustomerType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'webpage.exercises': {
            'Meta': {'object_name': 'Exercises'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'position_number_on_main_page': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'show_on_main_page': ('django.db.models.fields.BooleanField', [], {}),
            'show_on_pricelist': ('django.db.models.fields.BooleanField', [], {}),
            'show_on_timetable': ('django.db.models.fields.BooleanField', [], {})
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