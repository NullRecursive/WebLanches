from django.contrib import admin
from .models import Usuario, Produto, Pedido, Item   
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Produto)
#admin.site.register(Pedido) # para testes   
#admin.site.register(Item)