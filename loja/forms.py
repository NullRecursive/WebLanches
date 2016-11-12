from django import forms
'''
class FormCadastro(forms.Form):
	 nome = forms.CharField()
	 email = forms.EmailField()
	 senha = forms.CharField(widget=forms.PasswordInput)
	 csenha  = forms.CharField(widget=forms.PasswordInput)
	 endereco = forms.CharField()
	 username = forms.CharField()
	 cpf = forms.CharField(max_lenght = 11)
	 telefone = forms.CharField(max_lenght = 14)

