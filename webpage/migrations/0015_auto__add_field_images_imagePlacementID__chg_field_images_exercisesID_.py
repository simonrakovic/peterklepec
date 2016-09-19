# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Images.imagePlacementID'
        db.add_column(u'webpage_images', 'imagePlacementID',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['webpage.ImagePlacement']),
                      keep_default=False)


        # Changing field 'Images.exercisesID'
        db.alter_column(u'webpage_images', 'exercisesID_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webpage.Exercises']))
        # Deleting field 'ImagePlacement.exercisesID'
        db.delete_column(u'webpage_imageplacement', 'exercisesID_id')

        # Deleting field 'ImagePlacement.where_to_show'
        db.delete_column(u'webpage_imageplacement', 'where_to_show')


    def backwards(self, orm):
        # Deleting field 'Images.imagePlacementID'
        db.delete_column(u'webpage_images', 'imagePlacementID_id')


        # Changing field 'Images.exercisesID'
        db.alter_column(u'webpage_images', 'exercisesID_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webpage.ImagePlacement']))
        # Adding field 'ImagePlacement.exercisesID'
        db.add_column(u'webpage_imageplacement', 'exercisesID',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['webpage.Exercises']),
                      keep_default=False)

        # Adding field 'ImagePlacement.where_to_show'
        db.add_column(u'webpage_imageplacement', 'where_to_show',
                      self.gf('django.db.models.fields.IntegerField')(default=None),
                      keep_default=False)


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'priceUnit': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'pricingPlanID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webpage.PricingPlan']"}),
            'subscriptionLengthID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webpage.SubscriptionLength']"})
        },
        u'webpage.pricingplan': {
            'Meta': {'object_name': 'PricingPlan'},
            'exercisesID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webpage.Exercises']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'webpage.subscriptionlength': {
            'Meta': {'object_name': 'SubscriptionLength'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lengthNumber': ('django.db.models.fields.IntegerField', [], {}),
            'lengthUnit': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['webpage']