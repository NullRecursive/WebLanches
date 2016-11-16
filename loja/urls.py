from django.conf.urls import url
from . import views

urlpatterns = [    
    url(r'^entrar/$', views.login_page, name = 'login'),
    url(r'^cadastrar/$', views.cad_page, name = 'cadastrar'),
    url(r'^cardapio/$', views.cardapio, name = 'cardapio'),
    url(r'^hamburguer/$', views.hamburguer, name = 'hamburguer'),
    url(r'^home/$', views.hamburguer, name = 'home'),
]
