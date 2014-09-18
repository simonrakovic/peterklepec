# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from webpage.admin import Novice


def home(request):

    allNews = Novice.objects.all()

    title = allNews[0].title
    content = allNews[0].content

    return render_to_response('webpages/home.html', locals(), context_instance=RequestContext(request))

def fitnes(request):
    return render_to_response('webpages/fitnes.html', locals(),context_instance=RequestContext(request))

def pricelist(request):
    return render_to_response('webpages/pricelist.html', locals(),context_instance=RequestContext(request))