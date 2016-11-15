from django import template

register = template.Library()

@register.filter(name='show_admin')
def show_admin(value):
    msg = ' - ADMIN'
    return value + msg