from django import forms
from django.core.exceptions import ValidationError

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
			attrs={'required': 'required'}))
	cep = forms.CharField(
		widget = forms.TextInput(
			attrs={'required': 'required'}))

	

class FormLogin(forms.Form):
	usuario = forms.CharField(
		max_length = 40)
	senha = forms.CharField(
		widget = forms.PasswordInput)
