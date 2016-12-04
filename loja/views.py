from .models import Usuario
from .forms import FormLogin, FormCadastro
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.template import loader
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
	template = loader.get_templates('template/hamburguer.html')
	context = {
		'all_produto' = all_produtos
	}
	return template.render(context,request, 'loja/hamburguer.html')

def sair(request):
	controller = ControllerUsuario()
	controller.logout(request)
	return redirect(cardapio)
