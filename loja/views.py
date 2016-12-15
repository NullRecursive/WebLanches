# -*- coding: utf-8 -*-
from .models import Usuario, Produto, Pedido, Item
from .forms import FormLogin, FormCadastro, FormStatus, FormProduto
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .controllers import ControllerUsuario
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .report import write_to_pdf

def home(request):
	return redirect(produto_tipo, tipo = 'todos')

def login_page(request):
	if request.user.is_authenticated():
		return redirect(home)

	if request.method == 'POST':
		form = FormLogin(request.POST)
		controller =  ControllerUsuario()
		if controller.logar(request, form):
			return redirect(home)
	else:
		form = FormLogin()

	return render(request,'loja/login/login.html', {'form': form})

def cad_page(request):
	if request.method == 'POST':
		form = FormCadastro(request.POST)
		controller = ControllerUsuario()
		if controller.cadastrar(request, form):
			messages.success(request, "Usuario criado com sucesso")
		else:
			messages.error(request, "Usuario ja existente!")
	else:
		form = FormCadastro()

	return render(request, 'loja/login/cadastro.html', {'form': form})

def cad_produto(request):
	if request.method == 'POST':
		form = FormProduto(request.POST, request.FILES)

		if form.is_valid():
			produto = Produto()
			produto.nome = form.cleaned_data["nome"]
			produto.preco = form.cleaned_data["preco"]
			produto.descricao = form.cleaned_data["descricao"]
			produto.imagem = form.cleaned_data["imagem"]
			produto.em_Falta = form.cleaned_data["em_Falta"]
			produto.categoria = form.cleaned_data["categoria"]
			produto.save()

			messages.success(request, "Procuto criado com sucesso ")
		else:
			messages.error(request, "Produto já existente!")
	else:
		form = FormProduto()

	return render(request, 'loja/cadastrar_produto.html', {'form': form})

def deleta_produto(request, id_nome):
	Produto.objects.filter(nome = id_nome).delete()
	return redirect(home)

def add_pedido(request, id_produto):
	if request.user.is_authenticated:
		if request.POST:
			usuario = request.user
			quantidade = int(request.POST.get('qtd_pedido'))
			produto = Produto.objects.get(nome = id_produto)

			pedido = None
			try:
				pedido = Pedido.objects.get(usuario = usuario.pk, estado_do_pedido = Pedido.ESTADO_PEDIDO[0][0])
			except ObjectDoesNotExist or Exception:
				pedido = Pedido(usuario = usuario)
				pedido.save()

			item = None
			try:
				item = Item.objects.get(id_pedido = pedido.pk, id_produto = id_produto, ativo = True)
				item.addQuantidade(quantidade)
				item.save()
			except ObjectDoesNotExist or Exception:
				item = Item(id_pedido = pedido, id_produto = produto, quantidade = quantidade)
				item.save()
			return redirect(pedidos_usuario)
	else:
		return redirect(login_page)


def produto_tipo(request, tipo):
	tipo_produtos = []
	if tipo == 'todos':
		tipo_produtos = Produto.objects.all()
	else:
		tipo_produtos = Produto.objects.filter(categoria = tipo)
	return render(request, 'loja/cardapio/tipo_produtos.html', {'produtos': tipo_produtos})

def sair(request):
	controller = ControllerUsuario()
	controller.sair(request)
	return redirect(home)


def pedidos_usuario(request):
	if not request.user.is_superuser:
		vazio = False
		usuario = request.user
		pedidos = Pedido.objects.filter(usuario = usuario.pk).order_by('-data_do_pedido')
		if len(pedidos) <= 0:
			vazio = True
		return render(request, 'loja/pedido/pedidos.html', {'pedidos' : pedidos, 'vazio' : vazio })
	return redirect(home)


def itens_pedido(request, id_pedido):
	vazio = False
	itens = Item.objects.filter(id_pedido = id_pedido)
	pedido = Pedido.objects.get(pk = id_pedido)
	state_pedido = pedido.estado_do_pedido
	usuario = Usuario.objects.get(username = pedido.usuario)

	if len(itens) <= 0:
		vazio = True
	return render(request, 'loja/pedido/itens_pedido.html',
		{'itens': itens,
		'id_pedido' : id_pedido,
		'status' : Pedido.ESTADO_PEDIDO,
		'state_pedido' : state_pedido,
		'vazio' : vazio,
		'usuario' : usuario.__str__,
		'endereco' : usuario.endereco,
		'cep' : usuario.cep })


def ver_comprovante(request, id_pedido):
	itens = Item.objects.filter(id_pedido = id_pedido)
	return render(request, 'loja/pedido/comprovante.html', {'itens': itens,'id_pedido':id_pedido})

def all_pedidos(request):
	if request.user.is_superuser:
		vazio = False
		pedidos = Pedido.objects.exclude(estado_do_pedido = Pedido.ESTADO_PEDIDO[0][0]).order_by('data_do_pedido')
		if len(pedidos) <= 0:
			vazio = True
		return render(request, 'loja/pedido/pedidos.html', {'pedidos' : pedidos, 'vazio' : vazio})
	return redirect(home)

def alter_status(request, id_pedido):
	if request.POST and request.user.is_superuser:
		status_key = request.POST.getlist('pedido_status')
		new_status = str(status_key[0])
		pedido = Pedido.objects.get(pk = id_pedido)
		pedido.estado_do_pedido = new_status
		pedido.save()
	return itens_pedido(request, id_pedido)

def concluir_pedido(request, id_pedido):
	pedido = Pedido.objects.get(pk = id_pedido)
	pedido.estado_do_pedido = Pedido.ESTADO_PEDIDO[1][0]
	pedido.save()
	return ver_comprovante(request,id_pedido)


def modificar_qtd_item(request, id_item, id_pedido):
	if request.POST:
		quantidade_nova = int(request.POST.get('qtd_item'))
		if quantidade_nova > 0:
			item = Item.objects.get(pk = id_item)
			item.quantidade = quantidade_nova
			item.save()
	return itens_pedido(request, id_pedido)

def cancelar_pedido(request, id_pedido):
	Item.objects.filter(id_pedido = id_pedido).delete()
	Pedido.objects.filter(pk = id_pedido).delete()
	return redirect(home)


def ver_pdf(request, id_pedido):
	pedido = Pedido.objects.get(id = id_pedido)
	usuario = Usuario.objects.get(username = pedido.usuario)
	itens =  Item.objects.filter(id_pedido = id_pedido)
	return write_to_pdf(request,'loja/pedido/template_comprovante.html',{'itens':itens,'usuario':usuario})

def buscar(request):
	vazio = False
	if request.POST:
		value_busca = str(request.POST.get('busca'))
		valores_busca = Produto.objects.filter(nome__icontains = value_busca)
		if len(valores_busca) <= 0:
			vazio = True
		return render(request, 'loja/cardapio/tipo_produtos.html', {'produtos': valores_busca, 'vazio' : vazio})
	return redirect(home)

def fazer_pedido(request):
	try:
		pedido = Pedido.objects.filter(
			usuario = request.user,
			estado_do_pedido = Pedido.ESTADO_PEDIDO[0][0])[0]
		return itens_pedido(request, pedido.pk)
	except IndexError:
		pedido = Pedido(usuario = request.user)
		pedido.save()
		return itens_pedido(request, pedido.pk)

def editar_perfil(request):
	if request.user.is_authenticated:
		usuario = Usuario.objects.get(username = request.user.username)
		if request.method == 'POST':
			form = FormCadastro(request.POST)
			controller = ControllerUsuario()
			if controller.editar_usuario(request, form):
				messages.success(request, "Informacões alteradas com sucesso")
			else:
				messages.error(request, "Erro ao editar informacões")
		else:
			form = FormCadastro()
		return render(request,'loja/editar_perfil.html',{'form':form,'usuario':usuario})