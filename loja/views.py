from .models import Usuario, Produto, Pedido, Item
from .forms import FormLogin, FormCadastro, FormStatus
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .controllers import ControllerUsuario

# -*- coding: utf-8 -*-
def home(request):
	return redirect(cardapio)

def login_page(request):
	if request.method == 'POST':
		form = FormLogin(request.POST)
		controller =  ControllerUsuario()
		if controller.logar(request,form):
			return redirect("/cardapio/")
	else:
		form = FormLogin()

	return render(request,'loja/login/login.html', {'form': form})

def cardapio(request):
	return redirect(produto_tipo, tipo = 'todos')

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

def add_pedido(request, id_produto, quantidade):
	usuario = request.Usuario #pega usuario da requisicao
	pedido = Pedido.objects.filter(usuario = usuario, estado_do_pedido = ESTADO_PEDIDO[0]) #pega TODOS pedidos do usuario
	item = Item(id_pedido = pedido.pk, id_produto = id_produto, quantidade = quantidade)
	item.save()
	return render(request, 'loja/pedido/pedidos.html')

def produto_tipo(request, tipo):
	tipo_produtos = []
	if tipo == 'todos':
		tipo_produtos = Produto.objects.all() 
	else:			
		tipo_produtos = Produto.objects.filter(categoria = tipo)
	return render(request, 'loja/cardapio/tipo_produtos.html', {'produtos': tipo_produtos})

def sair(request):
	controller = ControllerUsuario()
	controller.logout(request)
	return redirect(cardapio)

def add_produto_pedido(request, id_produto, quantidade):
	usuario = request.Usuario #pega usuario da requisicao
	pedido = Pedido.objects.filter(usuario = usuario, estado_do_pedido = ESTADO_PEDIDO[0]) #pega TODOS pedidos do usuario
	item = Item(id_pedido = pedido.pk, id_produto = id_produto, quantidade = quantidade)
	item.save
	return render(request, 'loja/pedido/pedidos.html')

def pedidos_usuario(request):
	if not request.user.is_superuser:
		usuario = request.user
		pedidos = Pedido.objects.filter(usuario = usuario.pk)
		return render(request, 'loja/pedido/pedidos.html', {'pedidos' : pedidos})
	return redirect(home)

def itens_pedido(request, id_pedido):
	itens = Item.objects.filter(id_pedido = id_pedido)
	produtos = Produto.objects.all()
	state_pedido = get_object_or_404(Pedido, pk = id_pedido).estado_do_pedido
	return render(request, 'loja/pedido/itens_pedido.html',
		{'itens': itens, 'id_pedido' : id_pedido, 'status' : Pedido.ESTADO_PEDIDO, 'state_pedido' : state_pedido})

def ver_comprovante(request,id_pedido):
	itens =  Item.objects.filter(id_pedido = id_pedido)
	dicionario = {}
	for item in itens:
		dicionario[item.id_produto] = Produto.objects.filter(nome = item.id_produto)
	return render(request,'loja/pedido/comprovante.html',{'dicionario': dicionario})

def all_pedidos(request):
	if request.user.is_superuser:
		pedidos = Pedido.objects.all()
		return render(request, 'loja/pedido/pedidos.html', {'pedidos' : pedidos})
	return redirect(home)

def alter_status(request, id_pedido):
	if request.POST and request.user.is_superuser:
		status_key = request.POST.getlist('pedido_status')
		new_status = str(status_key[0])

		pedido = get_object_or_404(Pedido, pk = id_pedido)
		pedido.estado_do_pedido = new_status
		pedido.save()

	return redirect(itens_pedido, id_pedido = id_pedido)
