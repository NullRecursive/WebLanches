from .models import Usuario
from .forms import FormCadastro

from django.shortcuts import render

def home_page(request):
	return render(request, 'loja/base.html')

def login_page(request):
	return render(request,'loja/login.html')

#incompleto
def cad_page(request):
	if request.method()=='POST':
		form = FormCadastro(request.POST)
		if form.is_valid():
			usuario = form.cleaned_data['username']
			nome = form.cleaned_data['nome']
			endereco = form.cleaned_data['endereco']
			telefone = form.cleaned_data['telefone']
			cpf = form.cleaned_data['cpf']
			senha = form.cleaned_data['senha']
			email = form.cleaned_data['email']
			user = Usuario()
			user.set_password(senha)
			user.name = nome;
			user.endereco = endereco
			user.telefone = telefone
			user.setCPF(cpf)
			user.setTelefone(telefone)


	return render(request,'loja/cadastro.html')

def cardapio(request):
	return render(request,'loja/cardapio.html')
