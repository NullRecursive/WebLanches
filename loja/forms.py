# -*- coding=utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from .models import Usuario, Pedido, Produto

class FormCadastro(forms.Form):
	nome = forms.CharField(
		widget = forms.TextInput(
			attrs={'autofocus': 'autofocus', 'required': 'required'}),
		max_length = 40)
	email = forms.EmailField(
		widget = forms.TextInput(
			attrs={'required': 'required'}))
	senha = forms.CharField(
		widget = forms.PasswordInput(
			attrs={'required' : 'required', 'onchange' : 'validarTamSenha(senha)'}))
	csenha  = forms.CharField(
		widget = forms.PasswordInput(
			attrs={'required' : 'required' , 'onchange' : 'validarSenha(senha, csenha)'}))
	endereco = forms.CharField(
		widget = forms.TextInput(
			attrs={'required': 'required'}))
	username = forms.CharField(
		widget = forms.TextInput(
			attrs={'required': 'required'}),
		max_length = 40)
	cpf = forms.CharField(
		widget = forms.TextInput(
			attrs={'required': 'required'}))
	telefone = forms.CharField(
		widget = forms.TextInput(
			attrs = {'required': 'required'}))
	cep = forms.CharField(
		widget = forms.TextInput(
			attrs={'required': 'required'}))

	class Meta:
		model = Usuario
		exclude = ['csenha']
		fields = ['nome', 'email', 'senha', 'username', 'telefone', 'cpf', 'endereco', 'cep']

	def clean_usuario(self):
		usuario_novo = self.cleaned_data['username']
		if User.objects.get_by_natural_key(username = usuario_novo) != None:
			raise forms.ValidationError(u'Usuário já existe!')
		else:
			return self.cleaned_data['username']

class FormProduto(forms.Form):
	nome = forms.CharField(
		widget = forms.TextInput(
			attrs={'autofocus': 'autofocus', 'required': 'required'}),
		max_length = 40)

	preco = forms.FloatField(
		widget = forms.TextInput(
			attrs={'required': 'required'}))

	descricao = forms.CharField(
		widget = forms.TextInput(
			attrs={'required' : 'required'}))
	imagem = forms.ImageField(required = False)

	em_Falta = forms.BooleanField(required=False)

	categoria =  forms.ChoiceField(choices = Produto.PRODUTOS)




class FormLogin(forms.Form):
	usuario = forms.CharField(
		max_length = 40)
	senha = forms.CharField(
		widget = forms.PasswordInput)


class FormStatus(forms.Form):
	status = forms.ChoiceField(choices = Pedido.ESTADO_PEDIDO)
