from .models import Usuario
from .forms import FormLogin, FormCadastro
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .controllers import ControllerUsuario

def home(request):
	return redirect(cardapio)

def cardapio(request):
	return redirect(hamburguer)

def login_page(request):
	if request.method == 'POST':
		form = FormLogin(request.POST)
		controller =  ControllerUsuario()
		if controller.logar(request,form):
			return redirect(cadapio)
		
	else:
		form = FormLogin()

	return render(request,'loja/login.html',{'form': form})


def cad_page(request):
	if request.method == 'POST':
		form = FormCadastro(request.POST) 
		controller = ControllerUsuario()
		controller.cadastrar(request, form)
	else:
		form = FormCadastro()

	return render(request, 'loja/cadastro.html', {'form': form})

def hamburguer(request):
	return render(request, 'loja/hamburguer.html')

def sair(request):
	controller = ControllerUsuario()
	controller.logout(request)
	return redirect(cardapio)
