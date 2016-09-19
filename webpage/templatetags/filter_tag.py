from django import template

register = template.Library()

@register.filter()
def in_pricing_plans(pricing_plans, exercise):
    return pricing_plans.filter(exercisesID=exercise.id)
