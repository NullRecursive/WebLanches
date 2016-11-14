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
		widget = forms.PasswordInput, 
		required = True,
		min_length = 4)
	csenha  = forms.CharField(
		widget = forms.PasswordInput, 
		required = True)
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

	
	def clean(self):
		cleaned_data = super(FormCadastro, self).clean()
		senha = self.cleaned_data['senha']
		csenha = self.cleaned_data['csenha']

		if senha and senha != csenha:
			raise forms.ValidationError("A senhas sao diferentes")
				

class FormLogin(forms.Form):
	usuario = forms.CharField(
		max_length = 40)
	senha = forms.CharField(
		widget = forms.PasswordInput)


