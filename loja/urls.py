from django.conf.urls import url
from . import views
from django.dispatch import receiver

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^entrar/$', views.login_page, name = 'login'),
    url(r'^sair$', views.sair, name = 'sair'),
    url(r'^cadastrar/$', views.cad_page, name = 'cadastrar'),

    url(r'^cardapio/(?P<tipo>[a-z]*)/$', views.produto_tipo, name = 'produto_tipo'),
    url(r'^add_pedido/(?P<id_produto>[a-zA-Z0-9\s]*)/$', views.add_pedido, name = 'add_pedido'),
    url(r'^cadastrar_produto/$', views.cad_produto, name = 'cadastrar_produto'),
    url(r'^deleta_produto/(?P<id_nome>[a-zA-Z0-9\s]*)/$', views.deleta_produto, name = 'deleta_produto'),


    url(r'^fazer_pedido/$', views.fazer_pedido, name = 'fazer_pedido'),
    url(r'^pedidos/$', views.pedidos_usuario, name = 'pedidos_usuario'),
    url(r'^pedido/(?P<id_pedido>[0-9]+)/itens/$', views.itens_pedido, name = 'itens_pedido'),
    url(r'^alter_status/(?P<id_pedido>[0-9]+)/$', views.alter_status, name = 'alter_status'),
    url(r'^concluir_pedido/(?P<id_pedido>[0-9]+)/$', views.concluir_pedido, name = 'concluir_pedido'),
    url(r'^modificar_qtd_item/(?P<id_item>[0-9]+)/(?P<id_pedido>[0-9]+)/$', views.modificar_qtd_item, name = 'modificar_qtd_item'),
    url(r'^cancelar_pedido/(?P<id_pedido>[0-9]+)/$', views.cancelar_pedido, name = 'cancelar_pedido'),

    url(r'^gerar_pdf/(?P<id_pedido>[0-9]+)/$',views.ver_pdf,name = 'ver_pdf'),
    url(r'^buscar/$', views.buscar, name = 'buscar'),
    url(r'^pedidos-gerenciamento/$', views.all_pedidos, name = 'all_pedidos'),
    url(r'^editar_perfil/$', views.editar_perfil, name = 'editar_perfil'),
]
