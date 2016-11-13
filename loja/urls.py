from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page),
    url(r'^entrar/$', views.login_page, name ='login'),
    url(r'^cadastrar/$', views.cad_page, name = 'cadastrar'),
    url(r'^cardapio/$', views.cardapio, name = 'cardapio'),
]
