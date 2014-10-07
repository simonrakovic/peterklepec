# Create your views here.
import pdb
import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from rest_framework import serializers,generics

from models import Images, Exercises, PricingPlan, Prices, CustomPage, News, ExercisesWeeklyTimetable, NotWorkingHours, \
    WeekDay


def home(request):
    leftMenuImages = Images.objects.filter(imagePlacementID=1).order_by('exercisesID__position_number_on_main_page')

    news = News.objects.all()
    return render_to_response('webpages/home.html', locals(), context_instance=RequestContext(request))


def offers(request, id):
    leftMenuImages = Images.objects.filter(imagePlacementID=1).order_by('exercisesID__position_number_on_main_page')

    exercise = Exercises.objects.get(pk=id)
    gallery_images = Images.objects.filter(exercisesID=exercise).filter(imagePlacementID=3)
    prices = Prices.objects.filter(pricingPlanID__exercisesID=exercise)
    num_of_pricingPlans = PricingPlan.objects.filter(exercisesID=exercise).count()
    num_of_prices = prices.count()

    #ker so v izgledu cene izpisane v skolpih po dva glede na pricingPlan, se lahko prikaze maxsimalno 2 pricingPlana
    if num_of_pricingPlans > 2 or prices.count() > 8:
        #ce ima vec kot 2 plana, se za pirkaz na ponudbeni strani izbere samo prvega
        #ce je vec kot 8 cen se izbere prvi plan in se stem zmanjsa stevilo prikazanih cen( pod pogojem da ima ponudba vec pricingPlanov)
        pricingPlans = PricingPlan.objects.filter(exercisesID=exercise)
        prices = Prices.objects.filter(pricingPlanID=pricingPlans[0])
        num_of_prices = prices.count()
        if prices.count() > 8:
            return render_to_response('webpages/offers2.html', locals(), context_instance=RequestContext(request))

    #zaradi izgleda spletne strani je omejen prikaz cen na strani, prikazano je lahko 8,4,2 ali 0 razlicnih cen (toliko je prostora)
    #ker je stevilo cen glede na ponudbo razlicno, so potrebni tudi razlicni prikazi, ki omogocajo prikaz razlicno ptevilo cen

    if prices.count() == 2: #omogoca prikaz 2 razlicnih cen
        first_part = prices.order_by('customerTypeID')[0]
        second_part = prices.order_by('customerTypeID')[1]
        return render_to_response('webpages/offers2.html', locals(), context_instance=RequestContext(request))

    elif prices.count() == 4: #omogoca prikaz 4 razlicnih cen
        first_part = prices.order_by('customerTypeID')[:2]
        second_part = prices.order_by('customerTypeID')[2:4]

        loop = zip(first_part, second_part)
        return render_to_response('webpages/offers2.html', locals(), context_instance=RequestContext(request))

    elif prices.count() == 8: #omogoca prikaz 8 razlicnih cen
        first_part = prices.order_by('customerTypeID')[:4]
        second_part = prices.order_by('customerTypeID')[4:8]

        loop = zip(first_part, second_part)
        return render_to_response('webpages/offers.html', locals(), context_instance=RequestContext(request))

    else: #omogoca prikaz, ki ne izpolnjuje zgornje pogoje
        return render_to_response('webpages/offers2.html', locals(), context_instance=RequestContext(request))


def pricelist(request):
    leftMenuImages = Images.objects.filter(imagePlacementID=1).order_by('exercisesID__position_number_on_main_page')

    active_id = 1
    exercises = Exercises.objects.all()
    pricing_plans = PricingPlan.objects.all()
    prices = Prices.objects.all().order_by('customerTypeID')

    return render_to_response('webpages/pricelist.html', locals(), context_instance=RequestContext(request))


def timetable(request):
    leftMenuImages = Images.objects.filter(imagePlacementID=1).order_by('exercisesID__position_number_on_main_page')
    exercises = Exercises.objects.all()
    active_id = 1
    return render_to_response('webpages/timetable.html', locals(), context_instance=RequestContext(request))


def custompage(request, id):
    leftMenuImages = Images.objects.filter(imagePlacementID=1).order_by('exercisesID__position_number_on_main_page')

    custompage = CustomPage.objects.get(pk=id)
    if not custompage.active:
        raise Http404
    return render_to_response('webpages/'+custompage.pageLayoutID.template_path, locals(), context_instance=RequestContext(request))


# restfullAPI za posiljanje JSON za avtomatsko refreshanje urnika (AJAX princip)
#serializer za serializacijo modela v JSON format
class WeekDaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekDay
        fields = ('day_in_week',)

class ExercisesWeeklyTimetableSerializer(serializers.ModelSerializer):
    """Serializes a User object"""
    weekDay = WeekDaysSerializer()

    class Meta:
        model = ExercisesWeeklyTimetable


class NotWorkingHoursSerializer(serializers.ModelSerializer):
    """Serializes a User object"""
    class Meta:
        model = NotWorkingHours


#imprtanje classa generic iz django-rest-framework, ki poskrbi za GET request in posreduje zeljeni model v JSON oblik
class ExercisesWeeklyTimetableList(generics.ListAPIView):
    serializer_class = ExercisesWeeklyTimetableSerializer

    def get_queryset(self):
        return ExercisesWeeklyTimetable.objects.filter(exercisesID__pk=self.kwargs.get('id')).order_by('weekDay__day_in_week')


class NotWorkingHoursList(generics.ListAPIView):
    serializer_class = NotWorkingHoursSerializer

    def get_queryset(self):
        current_date = datetime.date.today()
        return NotWorkingHours.objects.filter(date__gte=current_date).filter(exercisesID__pk=self.kwargs.get('id')).order_by('date')
