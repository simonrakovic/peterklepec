# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Prices'
        db.create_table(u'webpage_prices', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pricingPlanID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webpage.PricingPlan'])),
            ('subscriptionLengthID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webpage.SubscriptionLength'])),
            ('customerTypeID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webpage.CustomerType'])),
            ('price', self.gf('django.db.models.fields.BooleanField')()),
            ('priceUnit', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'webpage', ['Prices'])

        # Adding model 'SubscriptionLength'
        db.create_table(u'webpage_subscriptionlength', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lengthUnit', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('lengthNumber', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'webpage', ['SubscriptionLength'])

        # Adding model 'CustomerType'
        db.create_table(u'webpage_customertype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'webpage', ['CustomerType'])

        # Adding model 'ExercisesWeeklyTimetable'
        db.create_table(u'webpage_exercisesweeklytimetable', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercisesID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webpage.Exercises'])),
            ('weekDay', self.gf('django.db.models.fields.IntegerField')()),
            ('timeFrom', self.gf('django.db.models.fields.TimeField')()),
            ('timeTo', self.gf('django.db.models.fields.TimeField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'webpage', ['ExercisesWeeklyTimetable'])

        # Adding model 'PricingPlan'
        db.create_table(u'webpage_pricingplan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercisesID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webpage.Exercises'])),
        ))
        db.send_create_signal(u'webpage', ['PricingPlan'])

        # Adding model 'Images'
        db.create_table(u'webpage_images', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercisesID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webpage.Exercises'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('placedIn', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webpage.ImagePlacement'])),
            ('imageDestination', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'webpage', ['Images'])

        # Adding model 'ImagePlacement'
        db.create_table(u'webpage_imageplacement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'webpage', ['ImagePlacement'])

        # Adding model 'NotWorkingHours'
        db.create_table(u'webpage_notworkinghours', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercisesID', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['webpage.Exercises'], null=True, blank=True)),
            ('weekDay', self.gf('django.db.models.fields.IntegerField')()),
            ('timeFrom', self.gf('django.db.models.fields.TimeField')()),
            ('timeTo', self.gf('django.db.models.fields.TimeField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'webpage', ['NotWorkingHours'])

        # Adding model 'Exercises'
        db.create_table(u'webpage_exercises', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('shown_on_main_page', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'webpage', ['Exercises'])


    def backwards(self, orm):
        # Deleting model 'Prices'
        db.delete_table(u'webpage_prices')

        # Deleting model 'SubscriptionLength'
        db.delete_table(u'webpage_subscriptionlength')

        # Deleting model 'CustomerType'
        db.delete_table(u'webpage_customertype')

        # Deleting model 'ExercisesWeeklyTimetable'
        db.delete_table(u'webpage_exercisesweeklytimetable')

        # Deleting model 'PricingPlan'
        db.delete_table(u'webpage_pricingplan')

        # Deleting model 'Images'
        db.delete_table(u'webpage_images')

        # Deleting model 'ImagePlacement'
        db.delete_table(u'webpage_imageplacement')

        # Deleting model 'NotWorkingHours'
        db.delete_table(u'webpage_notworkinghours')

        # Deleting model 'Exercises'
        db.delete_table(u'webpage_exercises')


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
            'shown_on_main_page': ('django.db.models.fields.BooleanField', [], {})
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
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'webpage.images': {
            'Meta': {'object_name': 'Images'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'exercisesID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webpage.Exercises']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageDestination': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'placedIn': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webpage.ImagePlacement']"})
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
        u'webpage.novice': {
            'Meta': {'object_name': 'Novice'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'webpage.prices': {
            'Meta': {'object_name': 'Prices'},
            'customerTypeID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webpage.CustomerType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.BooleanField', [], {}),
            'priceUnit': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'pricingPlanID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webpage.PricingPlan']"}),
            'subscriptionLengthID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webpage.SubscriptionLength']"})
        },
        u'webpage.pricingplan': {
            'Meta': {'object_name': 'PricingPlan'},
            'exercisesID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webpage.Exercises']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'webpage.subscriptionlength': {
            'Meta': {'object_name': 'SubscriptionLength'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lengthNumber': ('django.db.models.fields.IntegerField', [], {}),
            'lengthUnit': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['webpage']