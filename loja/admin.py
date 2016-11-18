from django.contrib import admin
from .models import Usuario
from .models import Produto
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Produto)