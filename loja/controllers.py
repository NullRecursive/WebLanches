from .models import Usuario, Pedido, Item, Produto
from django.contrib.auth import authenticate, login, logout
from django.db import models
from .forms import FormLogin, FormCadastro
from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import render, redirect
#contem as operacoes de usuario

class ControllerUsuario:

    def cadastrar(self, request, form):
    	form = FormCadastro(request.POST)

    	if form.is_valid():
            try:
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

            except IntegrityError:
                return False
            else:
                return True
        #return False # Ta com um erro FDP que nao reconhece

    def cadastrar_produto(self, request, form):
        form = FormProduto(request.POST)

        if form.is_valid():
            try:
                nome = form.cleaned_data['nome']
                preco = form.cleaned_data['preco']
                descricao = form.cleaned_data['descricao']
                em_falta = form.cleaned_data['em_Falta']


                produto = Produto()
                produto.nome =  nome
                produto.preco = preco
                produto.descricao = descricao
                produto.em_Falta = em_falta

                Produto.save(produto)

            except IntegrityError:
                return False
            else:
                return True

    def logar(self, request, form):
    	if form.is_valid():
       		usuario = form.cleaned_data['usuario']
       		senha = form.cleaned_data['senha']
       		user = authenticate(username = usuario, password = senha)
        	if user is not None:
	        	login(request, user)
	        	return True
	        return False
        
        
    def sair(self, request):
        logout(request)
