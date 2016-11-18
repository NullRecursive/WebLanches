from .models import Usuario
from django.contrib.auth import authenticate, login, logout

#contem as operacoes de usuario
class ControllerUsuario:
    
    def cadastrar(self,request,form):
	
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
        usuario = form.cleaned_data['usuario']
        senha = form.cleaned_data['senha']
        user = authenticate(username = usuario, password = senha)

        if user is not None:
            login(request, user)
            return True
        return False
        
    def logout(self, request):
        logout(request)

	
