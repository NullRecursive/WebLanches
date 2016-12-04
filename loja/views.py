from .models import Usuario
from .models import Produto
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
	all_produtos = Produto.objects.all()
	return render(request, 'loja/hamburguer.html', {'all_produtos': all_produtos})

def bebida(request):
	all_produtos = Produto.objects.all()
	return render(request, 'loja/bebida.html', {'all_produtos': all_produtos})

def pastel(request):
	all_produtos = Produto.objects.all()
	return render(request, 'loja/pastel.html', {'all_produtos': all_produtos})

def todos(request):
	all_produtos = Produto.objects.all()
	return render(request, 'loja/todos.html', {'all_produtos': all_produtos})

def sair(request):
	controller = ControllerUsuario()
	controller.logout(request)
	return redirect(cardapio)
