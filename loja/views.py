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

	return render(request,'loja/login/login.html', {'form': form})

def cardapio(request):
	return redirect(todos)

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

def hamburguer(request):
	produtos_hamburguer = Produto.objects.filter(categoria = 'hamburguer')
	return render(request, 'loja/cardapio/hamburguer.html', {'produtos_hamburguer': produtos_hamburguer})

def bebida(request):
	produtos_bebida = Produto.objects.filter(categoria = 'bebida')
	return render(request, 'loja/cardapio/bebida.html', {'produtos_bebida': produtos_bebida})

def pastel(request):
	produtos_pastel = Produto.objects.filter(categoria = 'pastel')
	return render(request, 'loja/cardapio/pastel.html', {'produtos_pastel': produtos_pastel})

def pizza(request):
	produtos_pizza = Produto.objects.filter(categoria = 'pizzas')
	return render(request, 'loja/cardapio/pizza.html', {'produtos_pizza': produtos_pizza})

def todos(request):
	all_produtos = Produto.objects.all()
	return render(request, 'loja/cardapio/todos.html', {'all_produtos': all_produtos})

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
	return render(request, 'loja/pedido/itens_pedido.html', {'itens': itens, 'produtos' : produtos})

def ver_comprovante(request,id_pedido):
	itens =  Item.objects.filter(id_pedido = id_pedido)
	return render(request,'loja/comprovante.html',{'itens': itens})

def all_pedidos(request):
	if request.user.is_superuser:
		pedidos = Pedido.objects.all()
		return render(request, 'loja/pedido/pedidos.html', {'pedidos' : pedidos })
	return redirect(home)

def salvar_modificacao_pedido(request):
	pass