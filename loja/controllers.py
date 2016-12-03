from .models import Usuario, Pedido, Item, Produto
from django.contrib.auth import authenticate, login, logout
from django.db import models
from .forms import FormLogin, FormCadastro
import json

#contem as operacoes de usuario
class ControllerUsuario:

    def cadastrar(self, request, form):
    	form = FormCadastro(request.POST)
    	if form.is_valid():
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

    def logar(self, request, form):
    	if form.is_valid():
       		usuario = form.cleaned_data['usuario']
       		senha = form.cleaned_data['senha']
       		user = authenticate(username = usuario, password = senha)
        	if user is not None:
	        	login(request, user)
	        	return True
	        return False

    def logout(self, request):
        logout(request)


class ControllerPedido:

	
	def salva_pedido(self, request):
		try:
			meu_pedido = Pedido()
			lista_de_pedidos = get_all_pedidos()
			meu_pedido.meus_itens = json.dumps(lista_de_pedidos)
			meu_pedido.save()
			return True
		except Exception:
			return False
    


"""
		MANDAR PRO BANCO
		import simplejson as json # this would be just 'import json' in Python 2.7 and later


		myModel = MyModel()
		listIWantToStore = [1,2,3,4,5,'hello']
		myModel.myList = json.dumps(listIWantToStore)
		myModel.save()

		ACESSAR ELEMENTO
		jsonDec = json.decoder.JSONDecoder()
		myPythonList = jsonDec.decode(myModel.myList)
"""
