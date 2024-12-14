from django import template

register = template.Library()


@register.filter
def user_liked_workout(workout, user):
    return workout.like_set.filter(user=user).exists()
