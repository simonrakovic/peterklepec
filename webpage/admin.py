
from django.contrib import admin


from models import Exercises, ExercisesWeeklyTimetable, ImagePlacement, Images, CustomerType, News, NotWorkingHours, Prices, PricingPlan, \
    ExercisesPageLayout, CustomPage, PageLayout


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

class PageLayoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'template_path')





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



