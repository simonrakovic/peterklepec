
from django.contrib import admin


from models import Exercises, ExercisesWeeklyTimetable, ImagePlacement, Images, CustomerType, News, NotWorkingHours, Prices, PricingPlan, \
    ExercisesPageLayout, CustomPage, PageLayout, ExerciseLength, SubExercises, InfoBar, ListOfRules
from peterklepec_webpage.settings import PROJECT_PATH


class CommonMedia:
  js = (
    'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
    '/static/javascript/editor.js',
  )
  css = {
    'all': ('/static/css/editor.css',),
  }


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_on_main_page', 'position_number_on_main_page')
    Media = CommonMedia

class ExercisesWeeklyTimetableAdmin(admin.ModelAdmin):
    list_display = ('weekDay', 'timeFrom', 'timeTo', 'description')

class ImagePlacementAdmin(admin.ModelAdmin):
    list_display = ('description',)

class ImagesAdmin(admin.ModelAdmin):

    list_display = ('name', 'description', 'imagePlacementID', 'exercisesID', 'image_tag',)
    readonly_fields = ('image_tag',)
    Media = CommonMedia


class CustomerTypeAdmin(admin.ModelAdmin):
    list_display = ('description',)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'image_background', 'page_link')

class NotWorkingHoursAdmin(admin.ModelAdmin):
    list_display = ('exercisesID', 'date', 'timeFrom', 'timeTo', 'description')

class PricesAdmin(admin.ModelAdmin):
    list_display = ('pricingPlanID', 'description', 'customerTypeID', 'price', 'priceUnit')

class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ('exercisesID', 'name')

class ExercisesPageLayoutAdmin(admin.ModelAdmin):
    list_display = ('description', )

class CustomPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'subtitle', 'content', 'active', 'image_background', 'pageLayoutID')
    Media = CommonMedia

class PageLayoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'template_path')

class ExerciseLengthAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_of_exercise', 'end_of_exercise')

class SubExercisesAdmin(admin.ModelAdmin):
    list_display = ('name',)

class InfobarAdmin(admin.ModelAdmin):
    list_display = ('info', 'isActive', 'description', 'barColor', 'barTime')

class ListOfRulesAdmin(admin.ModelAdmin):
    list_display = ('text',)
    Media = CommonMedia


admin.site.register(Exercises, ExerciseAdmin)
admin.site.register(ExercisesWeeklyTimetable, ExercisesWeeklyTimetableAdmin)
admin.site.register(ImagePlacement, ImagePlacementAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(CustomerType, CustomerTypeAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(NotWorkingHours, NotWorkingHoursAdmin)
admin.site.register(Prices, PricesAdmin)
admin.site.register(PricingPlan, PricingPlanAdmin)
admin.site.register(ExercisesPageLayout, ExercisesPageLayoutAdmin)
admin.site.register(CustomPage, CustomPageAdmin)
admin.site.register(PageLayout, PageLayoutAdmin)
admin.site.register(ExerciseLength, ExerciseLengthAdmin)
admin.site.register(SubExercises, SubExercisesAdmin)
admin.site.register(InfoBar, InfobarAdmin)
admin.site.register(ListOfRules, ListOfRulesAdmin)

