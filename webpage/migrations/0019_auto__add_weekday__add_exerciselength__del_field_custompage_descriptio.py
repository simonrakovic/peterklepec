# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WeekDay'
        db.create_table(u'webpage_weekday', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('day_in_week', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'webpage', ['WeekDay'])

        # Adding model 'ExerciseLength'
        db.create_table(u'webpage_exerciselength', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('start_of_exercise', self.gf('django.db.models.fields.TimeField')()),
            ('end_of_exercise', self.gf('django.db.models.fields.TimeField')()),
            ('slotInterval', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'webpage', ['ExerciseLength'])

        # Deleting field 'CustomPage.description'
        db.delete_column(u'webpage_custompage', 'description')

        # Adding field 'CustomPage.title'
        db.add_column(u'webpage_custompage', 'title',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=100),
                      keep_default=False)

        # Adding field 'CustomPage.subtitle'
        db.add_column(u'webpage_custompage', 'subtitle',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CustomPage.content'
        db.add_column(u'webpage_custompage', 'content',
                      self.gf('django.db.models.fields.TextField')(default=None),
                      keep_default=False)

        # Adding field 'CustomPage.image_background'
        db.add_column(u'webpage_custompage', 'image_background',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['webpage.Images']),
                      keep_default=False)

        # Deleting field 'News.content'
        db.delete_column(u'webpage_news', 'content')

        # Adding field 'News.subtitle'
        db.add_column(u'webpage_news', 'subtitle',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=100),
                      keep_default=False)


        # Changing field 'News.title'
        db.alter_column(u'webpage_news', 'title', self.gf('django.db.models.fields.CharField')(max_length=100))
        # Deleting field 'NotWorkingHours.weekDay'
        db.delete_column(u'webpage_notworkinghours', 'weekDay')

        # Adding field 'NotWorkingHours.date'
        db.add_column(u'webpage_notworkinghours', 'date',
                      self.gf('django.db.models.fields.DateField')(default=None),
                      keep_default=False)


        # Renaming column for 'ExercisesWeeklyTimetable.weekDay' to match new field type.
        db.rename_column(u'webpage_exercisesweeklytimetable', 'weekDay', 'weekDay_id')
        # Changing field 'ExercisesWeeklyTimetable.weekDay'
        db.alter_column(u'webpage_exercisesweeklytimetable', 'weekDay_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webpage.WeekDay']))
        # Adding index on 'ExercisesWeeklyTimetable', fields ['weekDay']
        db.create_index(u'webpage_exercisesweeklytimetable', ['weekDay_id'])

        # Adding field 'Exercises.length'
        db.add_column(u'webpage_exercises', 'length',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['webpage.ExerciseLength'], null=True, blank=True),
                      keep_default=False)


        # Changing field 'Exercises.description'
        db.alter_column(u'webpage_exercises', 'description', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):
        # Removing index on 'ExercisesWeeklyTimetable', fields ['weekDay']
        db.delete_index(u'webpage_exercisesweeklytimetable', ['weekDay_id'])

        # Deleting model 'WeekDay'
        db.delete_table(u'webpage_weekday')

        # Deleting model 'ExerciseLength'
        db.delete_table(u'webpage_exerciselength')

        # Adding field 'CustomPage.description'
        db.add_column(u'webpage_custompage', 'description',
                      self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'CustomPage.title'
        db.delete_column(u'webpage_custompage', 'title')

        # Deleting field 'CustomPage.subtitle'
        db.delete_column(u'webpage_custompage', 'subtitle')

        # Deleting field 'CustomPage.content'
        db.delete_column(u'webpage_custompage', 'content')

        # Deleting field 'CustomPage.image_background'
        db.delete_column(u'webpage_custompage', 'image_background_id')

        # Adding field 'News.content'
        db.add_column(u'webpage_news', 'content',
                      self.gf('django.db.models.fields.TextField')(default=None),
                      keep_default=False)

        # Deleting field 'News.subtitle'
        db.delete_column(u'webpage_news', 'subtitle')


        # Changing field 'News.title'
        db.alter_column(u'webpage_news', 'title', self.gf('django.db.models.fields.TextField')())
        # Adding field 'NotWorkingHours.weekDay'
        db.add_column(u'webpage_notworkinghours', 'weekDay',
                      self.gf('django.db.models.fields.IntegerField')(default=None),
                      keep_default=False)

        # Deleting field 'NotWorkingHours.date'
        db.delete_column(u'webpage_notworkinghours', 'date')


        # Renaming column for 'ExercisesWeeklyTimetable.weekDay' to match new field type.
        db.rename_column(u'webpage_exercisesweeklytimetable', 'weekDay_id', 'weekDay')
        # Changing field 'ExercisesWeeklyTimetable.weekDay'
        db.alter_column(u'webpage_exercisesweeklytimetable', 'weekDay', self.gf('django.db.models.fields.IntegerField')())
        # Deleting field 'Exercises.length'
        db.delete_column(u'webpage_exercises', 'length_id')


        # Changing field 'Exercises.description'
        db.alter_column(u'webpage_exercises', 'description', self.gf('django.db.models.fields.TextField')(default=None))

    models = {
        u'webpage.customertype': {
            'Meta': {'object_name': 'CustomerType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'webpage.custompage': {
            'Meta': {'object_name': 'CustomPage'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_background': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webpage.Images']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pageLayoutID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webpage.PageLayout']"}),
            'subtitle': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'webpage.exerciselength': {
            'Meta': {'object_name': 'ExerciseLength'},
            'end_of_exercise': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slotInterval': ('django.db.models.fields.TimeField', [], {}),
            'start_of_exercise': ('django.db.models.fields.TimeField', [], {})
        },
        u'webpage.exercises': {
            'Meta': {'object_name': 'Exercises'},
            'description': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'exercises_page_layout': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['webpage.ExercisesPageLayout']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['webpage.ExerciseLength']", 'null': 'True', 'blank': 'True'}),
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
            'weekDay': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webpage.WeekDay']"})
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_background': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webpage.Images']"}),
            'page_link': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['webpage.CustomPage']", 'null': 'True', 'blank': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'webpage.notworkinghours': {
            'Meta': {'object_name': 'NotWorkingHours'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'exercisesID': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['webpage.Exercises']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timeFrom': ('django.db.models.fields.TimeField', [], {}),
            'timeTo': ('django.db.models.fields.TimeField', [], {})
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
        },
        u'webpage.weekday': {
            'Meta': {'object_name': 'WeekDay'},
            'day_in_week': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['webpage']