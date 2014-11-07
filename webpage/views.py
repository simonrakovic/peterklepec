# Create your views here.
import pdb
import datetime
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from rest_framework import serializers,generics

from models import Images, Exercises, PricingPlan, Prices, CustomPage, News, ExercisesWeeklyTimetable, NotWorkingHours, \
    WeekDay, SubExercises, CustomerType
from webpage.forms import QuestionForm


def home(request):
    leftMenuImages = Images.objects.filter(imagePlacementID=1).order_by('exercisesID__position_number_on_main_page')
    rightMenuImages = Images.objects.filter(imagePlacementID=2).order_by('exercisesID__position_number_on_main_page')

    current_week_day = datetime.datetime.today().weekday()+1
    current_time = datetime.datetime.now().time()
    fitness_working_hours = ExercisesWeeklyTimetable.objects.filter(exercisesID__name__contains="fitnes").filter(weekDay=current_week_day).filter(timeFrom__lte=current_time).filter(timeTo__gte=current_time)
    exercises_working_hours = ExercisesWeeklyTimetable.objects.filter(exercisesID__subexerciseID=1).filter(weekDay=current_week_day).filter(timeFrom__lte=current_time).filter(timeTo__gte=current_time)



    news = News.objects.all()
    return render_to_response('webpages/home.html', locals(), context_instance=RequestContext(request))


def offers(request, id):
    leftMenuImages = Images.objects.filter(imagePlacementID=1).order_by('exercisesID__position_number_on_main_page')
    rightMenuImages = Images.objects.filter(imagePlacementID=2).order_by('exercisesID__position_number_on_main_page')

    current_week_day = datetime.datetime.today().weekday()+1
    current_time = datetime.datetime.now().time()
    fitness_working_hours = ExercisesWeeklyTimetable.objects.filter(exercisesID__name__contains="fitnes").filter(weekDay=current_week_day).filter(timeFrom__lte=current_time).filter(timeTo__gte=current_time)
    exercises_working_hours = ExercisesWeeklyTimetable.objects.filter(exercisesID__subexerciseID=1).filter(weekDay=current_week_day).filter(timeFrom__lte=current_time).filter(timeTo__gte=current_time)

    exercise = Exercises.objects.get(pk=id)
    gallery_images = Images.objects.filter(exercisesID=exercise).filter(imagePlacementID=3)
    prices = Prices.objects.filter(pricingPlanID__exercisesID=exercise)
    num_of_pricingPlans = PricingPlan.objects.filter(exercisesID=exercise).count()

    if exercise.subexerciseID and exercise.subexercise_prices:
        prices = Prices.objects.filter(pricingPlanID__exercisesID=exercise.subexerciseID.exercisesID)
        num_of_pricingPlans = PricingPlan.objects.filter(exercisesID=exercise.subexerciseID.exercisesID).count()

    num_of_prices = prices.count()

    if exercise.has_subexercise:
        return suboffers(request, id)

    if exercise.exercises_page_layout.id == 4:
        return HttpResponseRedirect('/galerija_slik')

    if exercise.exercises_page_layout.id == 6:
        return HttpResponseRedirect('/vprasanja')

    if exercise.exercises_page_layout.id == 7:
        return HttpResponseRedirect('/dosezki')

    if exercise.exercises_page_layout.id == 3:
        return render_to_response('webpages/offers2.html', locals(), context_instance=RequestContext(request))


    #ker so v izgledu cene izpisane v skolpih po dva glede na pricingPlan, se lahko prikaze maxsimalno 2 pricingPlana
    if num_of_pricingPlans >= 2 and prices.count() > 8:
        #ce ima vec kot 2 plana, se za pirkaz na ponudbeni strani izbere samo prvega
        #ce je vec kot 8 cen se izbere prvi plan in se stem zmanjsa stevilo prikazanih cen( pod pogojem da ima ponudba vec pricingPlanov)


        pricingPlans = PricingPlan.objects.filter(exercisesID=exercise)
        if exercise.subexerciseID and exercise.subexercise_prices:
            pricingPlans = PricingPlan.objects.filter(exercisesID=exercise.subexerciseID.exercisesID)

        num_of_prices = 0
        prices = None
        for pricingPlan in pricingPlans:
            temp = Prices.objects.filter(pricingPlanID=pricingPlan)
            if num_of_prices < temp.count():
                prices = temp

        num_of_prices = prices.count()


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

def suboffers(request, id):
    leftMenuImages = Images.objects.filter(imagePlacementID=1).order_by('exercisesID__position_number_on_main_page')
    rightMenuImages = Images.objects.filter(imagePlacementID=2).order_by('exercisesID__position_number_on_main_page')

    current_week_day = datetime.datetime.today().weekday()+1
    current_time = datetime.datetime.now().time()
    fitness_working_hours = ExercisesWeeklyTimetable.objects.filter(exercisesID__name__contains="fitnes").filter(weekDay=current_week_day).filter(timeFrom__lte=current_time).filter(timeTo__gte=current_time)
    exercises_working_hours = ExercisesWeeklyTimetable.objects.filter(exercisesID__subexerciseID=1).filter(weekDay=current_week_day).filter(timeFrom__lte=current_time).filter(timeTo__gte=current_time)

    subexercise = Exercises.objects.filter(subexerciseID__exercisesID=id)

    images = Images.objects.filter(exercisesID=subexercise).filter(imagePlacementID=5)

    return render_to_response('webpages/suboffer.html', locals(), context_instance=RequestContext(request))

def gallery(request):
    leftMenuImages = Images.objects.filter(imagePlacementID=1).order_by('exercisesID__position_number_on_main_page')
    rightMenuImages = Images.objects.filter(imagePlacementID=2).order_by('exercisesID__position_number_on_main_page')

    current_week_day = datetime.datetime.today().weekday()+1
    current_time = datetime.datetime.now().time()
    fitness_working_hours = ExercisesWeeklyTimetable.objects.filter(exercisesID__name__contains="fitnes").filter(weekDay=current_week_day).filter(timeFrom__lte=current_time).filter(timeTo__gte=current_time)
    exercises_working_hours = ExercisesWeeklyTimetable.objects.filter(exercisesID__subexerciseID=1).filter(weekDay=current_week_day).filter(timeFrom__lte=current_time).filter(timeTo__gte=current_time)

    images = Images.objects.filter(imagePlacementID=7)

    return render_to_response('webpages/gallery.html', locals(), context_instance=RequestContext(request))

def questions(request):
    leftMenuImages = Images.objects.filter(imagePlacementID=1).order_by('exercisesID__position_number_on_main_page')
    rightMenuImages = Images.objects.filter(imagePlacementID=2).order_by('exercisesID__position_number_on_main_page')

    current_week_day = datetime.datetime.today().weekday()+1
    current_time = datetime.datetime.now().time()
    fitness_working_hours = ExercisesWeeklyTimetable.objects.filter(exercisesID__name__contains="fitnes").filter(weekDay=current_week_day).filter(timeFrom__lte=current_time).filter(timeTo__gte=current_time)
    exercises_working_hours = ExercisesWeeklyTimetable.objects.filter(exercisesID__subexerciseID=1).filter(weekDay=current_week_day).filter(timeFrom__lte=current_time).filter(timeTo__gte=current_time)

    question_form = QuestionForm()

    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            name = question_form.cleaned_data['name']
            email = question_form.cleaned_data['email']
            text = question_form.cleaned_data['text']

            send_mail('Vprasanje - spletna stran', 'Ime: '+name+'\nE-postni naslov: '+email+'\n'+text, email, ['simonrakovic@gmail.com'], fail_silently=False)
            question_form = QuestionForm()
            return render_to_response('webpages/questions.html', locals(), context_instance=RequestContext(request))


    return render_to_response('webpages/questions.html', locals(), context_instance=RequestContext(request))

def achievements(request):
    leftMenuImages = Images.objects.filter(imagePlacementID=1).order_by('exercisesID__position_number_on_main_page')
    rightMenuImages = Images.objects.filter(imagePlacementID=2).order_by('exercisesID__position_number_on_main_page')

    current_week_day = datetime.datetime.today().weekday()+1
    current_time = datetime.datetime.now().time()
    fitness_working_hours = ExercisesWeeklyTimetable.objects.filter(exercisesID__name__contains="fitnes").filter(weekDay=current_week_day).filter(timeFrom__lte=current_time).filter(timeTo__gte=current_time)
    exercises_working_hours = ExercisesWeeklyTimetable.objects.filter(exercisesID__subexerciseID=1).filter(weekDay=current_week_day).filter(timeFrom__lte=current_time).filter(timeTo__gte=current_time)

    images = Images.objects.filter(imagePlacementID=6)

    return render_to_response('webpages/achievements.html', locals(), context_instance=RequestContext(request))

def pricelist(request):
    leftMenuImages = Images.objects.filter(imagePlacementID=1).order_by('exercisesID__position_number_on_main_page')
    rightMenuImages = Images.objects.filter(imagePlacementID=2).order_by('exercisesID__position_number_on_main_page')

    current_week_day = datetime.datetime.today().weekday()+1
    current_time = datetime.datetime.now().time()
    fitness_working_hours = ExercisesWeeklyTimetable.objects.filter(exercisesID__name__contains="fitnes").filter(weekDay=current_week_day).filter(timeFrom__lte=current_time).filter(timeTo__gte=current_time)
    exercises_working_hours = ExercisesWeeklyTimetable.objects.filter(exercisesID__subexerciseID=1).filter(weekDay=current_week_day).filter(timeFrom__lte=current_time).filter(timeTo__gte=current_time)


    exercises = Exercises.objects.filter(show_on_pricelist=True)
    pricing_plans = PricingPlan.objects.filter(exercisesID__show_on_pricelist=True)
    prices = Prices.objects.all().order_by('customerTypeID')

    customer_types = CustomerType.objects.all()

    return render_to_response('webpages/pricelist.html', locals(), context_instance=RequestContext(request))


def timetable(request, id):
    leftMenuImages = Images.objects.filter(imagePlacementID=1).order_by('exercisesID__position_number_on_main_page')
    rightMenuImages = Images.objects.filter(imagePlacementID=2).order_by('exercisesID__position_number_on_main_page')

    current_week_day = datetime.datetime.today().weekday()+1
    current_time = datetime.datetime.now().time()
    fitness_working_hours = ExercisesWeeklyTimetable.objects.filter(exercisesID__name__contains="fitnes").filter(weekDay=current_week_day).filter(timeFrom__lte=current_time).filter(timeTo__gte=current_time)
    exercises_working_hours = ExercisesWeeklyTimetable.objects.filter(exercisesID__subexerciseID=1).filter(weekDay=current_week_day).filter(timeFrom__lte=current_time).filter(timeTo__gte=current_time)

    active_exercise = Exercises.objects.get(pk=id)
    exercises = Exercises.objects.filter(show_on_timetable=True)
    not_working_events = NotWorkingHours.objects.filter(exercisesID=id)
    exercise_events = ExercisesWeeklyTimetable.objects.filter(exercisesID=id)

    return render_to_response('webpages/timetable.html', locals(), context_instance=RequestContext(request))

def info(request):
    leftMenuImages = Images.objects.filter(imagePlacementID=1).order_by('exercisesID__position_number_on_main_page')
    rightMenuImages = Images.objects.filter(imagePlacementID=2).order_by('exercisesID__position_number_on_main_page')

    current_week_day = datetime.datetime.today().weekday()+1
    current_time = datetime.datetime.now().time()
    fitness_working_hours = ExercisesWeeklyTimetable.objects.filter(exercisesID__name__contains="fitnes").filter(weekDay=current_week_day).filter(timeFrom__lte=current_time).filter(timeTo__gte=current_time)
    exercises_working_hours = ExercisesWeeklyTimetable.objects.filter(exercisesID__subexerciseID=1).filter(weekDay=current_week_day).filter(timeFrom__lte=current_time).filter(timeTo__gte=current_time)

    return render_to_response('webpages/info.html', locals(), context_instance=RequestContext(request))

def custompage(request, id):
    leftMenuImages = Images.objects.filter(imagePlacementID=1).order_by('exercisesID__position_number_on_main_page')
    rightMenuImages = Images.objects.filter(imagePlacementID=2).order_by('exercisesID__position_number_on_main_page')

    current_week_day = datetime.datetime.today().weekday()+1
    current_time = datetime.datetime.now().time()
    fitness_working_hours = ExercisesWeeklyTimetable.objects.filter(exercisesID__name__contains="fitnes").filter(weekDay=current_week_day).filter(timeFrom__lte=current_time).filter(timeTo__gte=current_time)
    exercises_working_hours = ExercisesWeeklyTimetable.objects.filter(exercisesID__subexerciseID=1).filter(weekDay=current_week_day).filter(timeFrom__lte=current_time).filter(timeTo__gte=current_time)

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


