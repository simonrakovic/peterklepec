
from django.db import models
# Create your models here.


class Exercises(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    show_on_timetable = models.BooleanField()
    show_on_pricelist = models.BooleanField()
    exercises_page_layout = models.ForeignKey('ExercisesPageLayout', default=None, null=True, blank=True)

    show_on_main_page = models.BooleanField()
    position_number_on_main_page = models.IntegerField(default=None, null=True, blank=True)

    def __unicode__(self):
        return u'%s ' % self.name


class ExercisesPageLayout(models.Model):
    description = models.CharField(max_length=60)

    def __unicode__(self):
        return u'%s ' % self.description


class ExercisesWeeklyTimetable(models.Model):
    exercisesID = models.ForeignKey('Exercises')

    weekDay = models.ForeignKey('WeekDay')

    timeFrom = models.TimeField()
    timeTo = models.TimeField()

    description = models.TextField()

class WeekDay(models.Model):
    name = models.CharField(max_length=60)
    day_in_week = models.IntegerField()

    def __unicode__(self):
        return u'%s ' % self.name

class NotWorkingHours(models.Model):
    exercisesID = models.ForeignKey('Exercises', default=None, null=True, blank=True)

    date = models.DateField()
    timeFrom =models.TimeField()
    timeTo = models.TimeField()

    description = models.TextField()


class PricingPlan(models.Model):
    exercisesID = models.ForeignKey('Exercises')
    name = models.TextField()

    def __unicode__(self):
        return u'%s' % self.name


class Prices(models.Model):
    pricingPlanID = models.ForeignKey('PricingPlan')
    description = models.TextField()
    customerTypeID = models.ForeignKey('CustomerType')

    price = models.DecimalField(max_digits=6, decimal_places=2)

    priceUnit = models.CharField(max_length=10)


class CustomerType(models.Model):
    description = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s ' % self.description


class Images(models.Model):

    imagePlacementID = models.ForeignKey('ImagePlacement')
    exercisesID = models.ForeignKey('Exercises')

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    imageDestination = models.ImageField(upload_to='images/')

    def __unicode__(self):
        return u'%s' % self.name


class ImagePlacement(models.Model):
    description = models.TextField(default=None)

    def __unicode__(self):
        return u'%s' % self.description


class News(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)

    image_background = models.ForeignKey('Images')
    page_link = models.ForeignKey('CustomPage', default=None, null=True, blank=True)


class CustomPage(models.Model):

    name = models.CharField(max_length=50)

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, default=None, null=True, blank=True)
    content = models.TextField()

    image_background = models.ForeignKey('Images')

    active = models.BooleanField()
    pageLayoutID = models.ForeignKey('PageLayout')

    def __unicode__(self):
        return u'%s' % self.name


class PageLayout(models.Model):
    name = models.TextField()
    template_path = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.name

