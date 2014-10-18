
from django.db import models
# Create your models here.


class Exercises(models.Model):
    name = models.CharField(max_length=50, verbose_name='IME PONUDBE')
    description = models.TextField(verbose_name='OPIS PONUDBE', default=None, null=True, blank=True)

    show_on_timetable = models.BooleanField(verbose_name='PRIKAZI NA URNIKU')
    show_on_pricelist = models.BooleanField(verbose_name='PRIKAZI NA CENIKU')
    exercises_page_layout = models.ForeignKey('ExercisesPageLayout', default=None, null=True, blank=True, verbose_name='IZGLED OPISNE STRANI')

    show_on_main_page = models.BooleanField(verbose_name='PRIKAZI NA PRVI STRANI')
    position_number_on_main_page = models.IntegerField(default=None, null=True, blank=True, verbose_name='ZAPOREDNA STEVILKA PRIKAZA NA PRVI STRANI')

    length = models.ForeignKey('ExerciseLength', verbose_name='KDAJ SE PONUDBA IZVAJA')

    def __unicode__(self):
        return u'%s ' % self.name

    class Meta:
        verbose_name = 'Ponudba'
        verbose_name_plural = 'Ponudbe'

class ExerciseLength(models.Model):
    name = models.CharField(max_length=50)

    start_of_exercise = models.TimeField()
    end_of_exercise = models.TimeField()
    slotInterval = models.TimeField()

    def __unicode__(self):
        return u'%s ' % self.name

class ExercisesPageLayout(models.Model):
    description = models.CharField(max_length=60)

    def __unicode__(self):
        return u'%s ' % self.description


class ExercisesWeeklyTimetable(models.Model):
    exercisesID = models.ForeignKey('Exercises', verbose_name='IME PONUDBE')

    weekDay = models.ForeignKey('WeekDay', verbose_name='DAN IZVAJANJA')

    timeFrom = models.TimeField(verbose_name='ZACETEK IZVAJANJA')
    timeTo = models.TimeField(verbose_name='KONEC IZVAJANJA')

    description = models.TextField(verbose_name='OPIS')

    class Meta:
        verbose_name = 'Urnik ponudbe'
        verbose_name_plural = 'Urnik ponudb'

class WeekDay(models.Model):
    name = models.CharField(max_length=60)
    day_in_week = models.IntegerField()

    def __unicode__(self):
        return u'%s ' % self.name

class NotWorkingHours(models.Model):
    exercisesID = models.ForeignKey('Exercises', default=None, null=True, blank=True, verbose_name='IME PONUDBE')

    date = models.DateField(verbose_name='DATUM')
    timeFrom =models.TimeField(verbose_name='OD')
    timeTo = models.TimeField(verbose_name='DO')

    description = models.TextField(verbose_name='OPIS')

    class Meta:
        verbose_name = 'Odsotnost/rezervacija'
        verbose_name_plural = 'Odsotnosti/rezervacije'


class PricingPlan(models.Model):
    exercisesID = models.ForeignKey('Exercises', verbose_name='IME PONUDBE')
    name = models.TextField(verbose_name='IME PODZVRSTI CENIKA')

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = 'Podvrsta cenika'
        verbose_name_plural = 'Podvrsti cenika'


class Prices(models.Model):
    pricingPlanID = models.ForeignKey('PricingPlan', verbose_name='IME PODZVRSTI CENIKA')
    description = models.TextField(verbose_name='OPIS')
    customerTypeID = models.ForeignKey('CustomerType', verbose_name='VRSTA STRANKE')

    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='CENIA')

    priceUnit = models.CharField(max_length=10, verbose_name='DENARNA ENOTA')

    class Meta:
        verbose_name = 'Cena'
        verbose_name_plural = 'Cenik'


class CustomerType(models.Model):
    description = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s ' % self.description


class Images(models.Model):

    imagePlacementID = models.ForeignKey('ImagePlacement', verbose_name='LOKACIJA SLIKE')
    exercisesID = models.ForeignKey('Exercises', verbose_name='IME PONUDBE')

    name = models.CharField(max_length=50, verbose_name='IME SLIKE')
    description = models.TextField(blank=True, verbose_name='OPIS SLIKE')

    imageDestination = models.ImageField(upload_to='images/', verbose_name='NALOZI SLIKO')

    class Meta:
        verbose_name = 'Slika'
        verbose_name_plural = 'Slike'

    def __unicode__(self):
        return u'%s' % self.name


class ImagePlacement(models.Model):
    description = models.TextField(default=None)

    def __unicode__(self):
        return u'%s' % self.description


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='NASLOV')
    subtitle = models.CharField(max_length=100, verbose_name='PODNASLOV')

    image_background = models.ForeignKey('Images', verbose_name='SLIKA ZA OZADJE')
    page_link = models.ForeignKey('CustomPage', default=None, null=True, blank=True, verbose_name='LINK DO STRANI')

    class Meta:
        verbose_name = 'Novica'
        verbose_name_plural = 'Novice'


class CustomPage(models.Model):

    name = models.CharField(max_length=50, verbose_name='IME')

    title = models.CharField(max_length=100, verbose_name='NASLOV')
    subtitle = models.CharField(max_length=100, default=None, null=True, blank=True, verbose_name='PODNASLOV')
    content = models.TextField(verbose_name='BESEDILO')

    image_background = models.ForeignKey('Images', verbose_name='SLIKA ZA OZADJE')

    active = models.BooleanField(verbose_name='STRAN JE AKTIVNA')
    pageLayoutID = models.ForeignKey('PageLayout', verbose_name='IZGLED STRANI')

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = 'Nova stran'
        verbose_name_plural = 'Nove strani'

class PageLayout(models.Model):
    name = models.TextField()
    template_path = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.name

