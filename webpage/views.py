# Create your views here.
import pdb
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Images, Exercises, PricingPlan, Prices


def home(request):

    leftMenuImages = Images.objects.filter(imagePlacementID=1).order_by('exercisesID__position_number_on_main_page')
    return render_to_response('webpages/home.html', locals(), context_instance=RequestContext(request))

def offers(request, id):
    leftMenuImages = Images.objects.filter(imagePlacementID=1).order_by('exercisesID__position_number_on_main_page')

    exercise = Exercises.objects.get(pk=id)
    gallery_images = Images.objects.filter(imagePlacementID=3)
    prices = Prices.objects.filter(pricingPlanID__exercisesID=exercise)
    num_of_pricingPlans = PricingPlan.objects.filter(exercisesID=exercise).count()

    #ker so v izgledu cene izpisane v skolpih po dva glede na pricingPlan, se lahko prikaze maxsimalno 2 pricingPlana
    if num_of_pricingPlans > 2 or prices.count() > 8:
        #ce ima vec kot 2 plana, se za pirkaz na ponudbeni strani izbere samo prvega
        #ce je vec kot 8 cen se izbere prvi plan in se stem zmanjsa stevilo prikazanih cen( pod pogojem da ima ponudba vec pricingPlanov)
        pricingPlans = PricingPlan.objects.filter(exercisesID=exercise)
        prices = Prices.objects.filter(pricingPlanID=pricingPlans[0])
        if prices.count() > 8:
            return render_to_response('webpages/offers2.html', locals(), context_instance=RequestContext(request))

    #zaradi izgleda spletne strani je omejen prikaz cen na strani, prikazano je lahko 8,4,2 ali 0 razlicnih cen (toliko je prostora)
    #ker je stevilo cen glede na ponudbo razlicno, so potrebni tudi razlicni prikazi, ki omogocajo prikaz razlicno ptevilo cen

    if prices.count() == 2: #omogoca prikaz 2 razlicnih cen
        return render_to_response('webpages/offers2.html', locals(), context_instance=RequestContext(request))

    elif prices.count() == 4: #omogoca prikaz 4 razlicnih cen
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
    return render_to_response('webpages/pricelist.html', locals(), context_instance=RequestContext(request))

def timetable(request):
    leftMenuImages = Images.objects.filter(imagePlacementID=1).order_by('exercisesID__position_number_on_main_page')
    return render_to_response('webpages/timetable.html', locals(), context_instance=RequestContext(request))