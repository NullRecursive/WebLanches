from django import forms
from django.core.exceptions import ValidationError

class FormCadastro(forms.Form):
	nome = forms.CharField(
		widget = forms.TextInput(
			attrs={'autofocus': 'autofocus', 'required': 'required'}))
	email = forms.EmailField(
		widget = forms.TextInput(
			attrs={'required': 'required'}))
	senha = forms.CharField(
		widget = forms.PasswordInput)
	csenha  = forms.CharField(
		widget = forms.PasswordInput)
	endereco = forms.CharField(
		widget = forms.TextInput(
			attrs={'required': 'required'}))
	username = forms.CharField(
		widget = forms.TextInput(
			attrs={'required': 'required'}))
	cpf = forms.CharField(
		widget = forms.TextInput(
			attrs={'required': 'required'}))
	telefone = forms.CharField(
		widget = forms.TextInput(
			attrs={'required': 'required'}))
	cep = forms.CharField(
		widget = forms.TextInput(
			attrs={'required': 'required'}))


	def clean_pass(self):
		cleaned_data = super(FormCadastro, self).clean()
		senha = cleaned_data.get("senha")
		csenha = cleaned_data.get("csenha")
		
		#if len(senha) < 4:
		#	raise forms.ValidationError("A senha deve ter no minimo 4 caracteres")
			
		if senha and senha != csenha:
			raise forms.ValidationError(
				self.error_messages["A senhas sao diferentes"])


class FormLogin(forms.Form):
	usuario = forms.CharField()
	senha = forms.CharField(
		widget = forms.PasswordInput)
