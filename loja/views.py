from .models import Usuario, Produto, Pedido, Item
from .forms import FormLogin, FormCadastro
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .controllers import ControllerUsuario


def home(request):
	return redirect(cardapio)

def login_page(request):
	if request.method == 'POST':
		form = FormLogin(request.POST)
		controller =  ControllerUsuario()
		if controller.logar(request,form):
			return redirect(cardapio)

	else:
		form = FormLogin()

	return render(request,'loja/login.html',{'form': form})

def cardapio(request):
	return redirect(hamburguer)

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

	return render(request, 'loja/cadastro.html', {'form': form})

def hamburguer(request):
	produtos_hamburguer = Produto.objects.filter(categoria = 'hamburguer')
	return render(request, 'loja/hamburguer.html', {'produtos_hamburguer': produtos_hamburguer})

def bebida(request):
	produtos_bebida = Produto.objects.filter(categoria = 'bebida')
	return render(request, 'loja/bebida.html', {'produtos_bebida': produtos_bebida})

def pastel(request):
	produtos_pastel = Produto.objects.filter(categoria = 'pastel')
	return render(request, 'loja/pastel.html', {'produtos_pastel': produtos_pastel})

def pizza(request):
	produtos_pizza = Produto.objects.filter(categoria = 'pizzas')
	return render(request, 'loja/pizza.html', {'produtos_pizza': produtos_pizza})

def todos(request):
	all_produtos = Produto.objects.all()
	return render(request, 'loja/todos.html', {'all_produtos': all_produtos})

def sair(request):
	controller = ControllerUsuario()
	controller.logout(request)
	return redirect(cardapio)

def add_produto_pedido(request, id_produto, quantidade):
	usuario = request.Usuario #pega usuario da requisicao
	pedido = Pedido.objects.filter(usuario = usuario, ) #pega TODOS pedidos do usuario
	item = Item(pedido.pk, id_produto, quantidade)
	return render(request, 'loja/pedido.html')