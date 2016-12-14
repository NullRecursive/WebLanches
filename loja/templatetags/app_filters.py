from django import template
from loja.models import Item
import loja.views
register = template.Library()

@register.filter(name='show_admin')
def show_admin(value):
    msg = ' - ADMIN'
    return value + msg

@register.filter(name='total_pedido')
def get_total(pedido):
	return Item.total(pedido)
