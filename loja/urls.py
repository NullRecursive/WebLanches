from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^entrar/$', views.login_page, name = 'login'),
    url(r'^cadastrar/$', views.cad_page, name = 'cadastrar'),
    url(r'^cardapio/$', views.cardapio, name = 'cardapio'),
    url(r'^cardapio/hamburguer/$', views.hamburguer, name = 'hamburguer'),
    url(r'^cardapio/bebida/$', views.bebida, name = 'bebida'),
    url(r'^cardapio/pastel/$', views.pastel, name = 'pastel'),
    url(r'^cardapio/todos/$', views.todos, name = 'todos os produtos'),
    url(r'^sair$', views.sair, name = 'sair'),
]
