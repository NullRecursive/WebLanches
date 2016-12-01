from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.home, name = 'cardapio'),
    url(r'^cardapio/hamburguer/$', views.hamburguer, name = 'hamburguer'),
    url(r'^entrar/$', views.login_page, name = 'login'),
    url(r'^cadastrar/$', views.cad_page, name = 'cadastrar'),
    url(r'^sair$', views.sair, name = 'sair'),
]
