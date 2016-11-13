from .models import Usuario
from .forms import FormCadastro
from django.shortcuts import render

def home_page(request):
	return render(request, 'loja/base.html')

def login_page(request):
	return render(request,'loja/login.html')

# falta tratar a excessao de username repetido
def cad_page(request):
	if request.method == 'POST':
		form = FormCadastro(request.POST)
		if(form.is_valid()):
			usuario = form.cleaned_data['username']
			email = form.cleaned_data['email']
			telefone = form.cleaned_data['telefone']
			nome = form.cleaned_data['nome']
			endereco = form.cleaned_data['endereco']
			senha = form.cleaned_data['senha']
			csenha = form.cleaned_data['csenha']
			cpf = form.cleaned_data['cpf']	
			cep = form.cleaned_data['cep']

			user = Usuario()
			user.set_password(senha)
			user.email = email
			user.telefone = telefone
			user.endereco = endereco
			user.first_name = nome
			user.cpf = cpf
			user.username = usuario
			user.cep = cep
			user.save()
	else:
		form = FormCadastro()
		
	return render(request,'loja/cadastro.html',{'form': form,})

def cardapio(request):
	return render(request,'loja/cardapio.html')
