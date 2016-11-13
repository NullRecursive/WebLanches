from .models import Usuario
from .forms import FormCadastro
from django.shortcuts import render
from .forms import FormLogin
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect

def home_page(request):
	return render(request, 'loja/base.html')

def login_page(request):
	if request.method == 'POST':
		usuario = request.POST['usuario']
		senha = request.POST['senha']
		user = authenticate(username=usuario, password=senha)
		if user is not None:
			login(request,user)
			return redirect("/cardapio/")
			
	else: 
		form = FormLogin()

	return render(request,'loja/login.html',{'form': form,})

	

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
			user.password =  senha
			user.email = email
			user.telefone = telefone
			user.endereco = endereco
			user.first_name = nome
			user.cpf = cpf
			user.username = usuario
			user.cep = cep
			Usuario.save(user)
	else:
		form = FormCadastro()
		
	return render(request,'loja/cadastro.html',{'form': form,})

def cardapio(request):
	return render(request,'loja/cardapio.html')
