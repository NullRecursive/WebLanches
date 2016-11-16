from .models import Usuario
from .forms import FormLogin, FormCadastro
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db import IntegrityError
from .controllers import ControllerUsuario
def home(request):
	return render(request, 'loja/home.html')

def login_page(request):
	if request.method == 'POST':
		form = FormLogin(request.POST)
		if form.is_valid():
			controller = ControllerUsuario()
			
			if controller.logar(request,form):
				 return redirect("/cardapio/")
	else:
		form = FormLogin()

	return render(request,'loja/login.html',{'form': form})


def cad_page(request):
	if request.method == 'POST':
		form = FormCadastro(request.POST)
		if form.is_valid():
			try: 
				controller = ControllerUsuario()
				controller.cadastrar(request,form)
			except IntegrityError: #messages not running
				 messages.error(request, "Usuario ja existente!")

	else:
		form = FormCadastro()

	return render(request, 'loja/cadastro.html', {'form': form})

def cardapio(request):
	return render(request, 'loja/cardapio.html')

def hamburguer(request):
	return render(request, 'loja/hamburguer.html')
