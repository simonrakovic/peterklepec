
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
        return u'%s ' % (self.name)


class ExercisesPageLayout(models.Model):
    description = models.CharField(max_length=60)

    def __unicode__(self):
        return u'%s ' % (self.description)

class ExercisesWeeklyTimetable(models.Model):
    exercisesID = models.ForeignKey('Exercises')

    weekDay = models.IntegerField()

    timeFrom = models.TimeField()
    timeTo = models.TimeField()

    description = models.TextField()




class NotWorkingHours(models.Model):
    exercisesID = models.ForeignKey('Exercises', default=None, null=True, blank=True)

    weekDay = models.IntegerField()

    timeFrom =models.TimeField()
    timeTo = models.TimeField()

    description = models.TextField()


class PricingPlan(models.Model):
    exercisesID = models.ForeignKey('Exercises')
    name = models.TextField()

    def __unicode__(self):
        return u'%s' % (self.name)


class Prices(models.Model):
    pricingPlanID = models.ForeignKey('PricingPlan')
    description = models.TextField()
    customerTypeID = models.ForeignKey('CustomerType')

    price = models.DecimalField(max_digits=6, decimal_places=2)

    priceUnit = models.CharField(max_length=10)



class CustomerType(models.Model):
    description = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s ' % (self.description)


class Images(models.Model):

    imagePlacementID = models.ForeignKey('ImagePlacement')
    exercisesID = models.ForeignKey('Exercises')

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    imageDestination = models.ImageField(upload_to='images/')




class ImagePlacement(models.Model):
    description = models.TextField(default=None)

    def __unicode__(self):
        return u'%s' % (self.description)

class News(models.Model):
    title = models.TextField()
    content = models.TextField()





