
from django.contrib import admin


from models import Exercises, ExercisesWeeklyTimetable, ImagePlacement, Images, CustomerType, News, NotWorkingHours, Prices, PricingPlan, \
    ExercisesPageLayout


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_on_main_page', 'position_number_on_main_page')


class ExercisesWeeklyTimetableAdmin(admin.ModelAdmin):
    list_display = ('weekDay', 'timeFrom', 'timeTo', 'description')

class ImagePlacementAdmin(admin.ModelAdmin):
    list_display = ('description',)

class ImagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'imagePlacementID', 'exercisesID')

class CustomerTypeAdmin(admin.ModelAdmin):
    list_display = ('description',)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

class NotWorkingHoursAdmin(admin.ModelAdmin):
    list_display = ('exercisesID', 'weekDay', 'timeFrom', 'timeTo', 'description')

class PricesAdmin(admin.ModelAdmin):
    list_display = ('pricingPlanID', 'description', 'customerTypeID', 'price', 'priceUnit')

class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ('exercisesID', 'name')

class ExercisesPageLayoutAdmin(admin.ModelAdmin):
    list_display = ('description', )




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


