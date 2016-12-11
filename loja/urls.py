from django.conf.urls import url
from . import views
from django.dispatch import receiver

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^entrar/$', views.login_page, name = 'login'),
    url(r'^sair$', views.sair, name = 'sair'),
    url(r'^cadastrar/$', views.cad_page, name = 'cadastrar'),

    url(r'^cardapio/(?P<tipo>[a-z]*)/$', views.produto_tipo, name = 'produto_tipo'),
    url(r'^add_pedido/(?P<id_produto>[A-Z]*)/$', views.add_pedido, name = 'add_pedido'),

    url(r'^pedidos/$', views.pedidos_usuario, name = 'pedidos_usuario'),
    url(r'^pedido/(?P<id_pedido>[0-9]+)/itens/$', views.itens_pedido, name = 'itens_pedido'),
    url(r'^alter_status/(?P<id_pedido>[0-9]+)/$', views.alter_status, name = 'alter_status'),

    url(r'^pedidos-gerenciamento/$', views.all_pedidos, name = 'all_pedidos'),
]
