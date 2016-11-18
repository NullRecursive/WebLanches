from django.shortcuts import render, redirect
from django.db import IntegrityError
from .forms import FormLogin, FormCadastro
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .controllers import ControllerUsuario

controller = ControllerUsuario()

def home(request):
	return render(request, 'loja/home.html')

def login_page(request):

	if request.method == 'POST':
		form = FormLogin(request.POST)
		if form.is_valid():
			
			if controller.logar(request,form):
				 return redirect('/cardapio/')
	else:
		form = FormLogin()

	return render(request,'loja/login.html',{'form': form})


def cad_page(request):
	if request.method == 'POST':
		form = FormCadastro(request.POST)
		if form.is_valid():
			try: 
				controller.cadastrar(request,form)
			except IntegrityError: #messages not running
				 messages.success(request, 'Usuario ja existente!')

	else:
		form = FormCadastro()

	return render(request, 'loja/cadastro.html', {'form': form})

def cardapio(request):
	return render(request, 'loja/cardapio.html')

def hamburguer(request):
	return render(request, 'loja/hamburguer.html')

def sair(request):
	controller.logout(request)
	return redirect(home)
