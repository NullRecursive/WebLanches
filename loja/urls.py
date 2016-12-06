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
    url(r'^cardapio/pizza/$', views.pizza, name = 'pizza'),
    url(r'^cardapio/todos/$', views.todos, name = 'todos'),
    url(r'^sair$', views.sair, name = 'sair'),
    url(r'^add_produto_pedido/$', views.add_produto_pedido, name = 'add_produto_pedido'),
    url(r'^pedidos/$', views.pedidos_usuario, name = 'pedidos_usuario'),
    url(r'^pedido/(?P<pk>[0-9]+)/itens/$', views.itens_pedido, name = itens_pedido),
]
