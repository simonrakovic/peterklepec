from webpage.models import novice
from django.contrib import admin


class Novice(novice):
    list_display=('title', 'content', 'image')

admin.site.register(novice)