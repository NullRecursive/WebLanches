from django import forms

class FormCadastro(forms.Form):
	 nome = forms.CharField(
		 widget = forms.TextInput(
			 attrs={'autofocus': 'autofocus', 'required': 'required'}))
	 email = forms.EmailField(
		 widget = forms.TextInput(
			 attrs={'required': 'required'}))
	 senha = forms.CharField(
		 widget = forms.PasswordInput(
			 attrs={'required': 'required'}))
	 csenha  = forms.CharField(
		 widget = forms.PasswordInput(
			 attrs={'required': 'required'}))
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

