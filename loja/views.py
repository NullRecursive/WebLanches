from django.shortcuts import render

def home_page(request):
	return render(request, 'loja/base.html')

def login_page(request):
	return render(request,'loja/login.html')

def cad_page(request):
	return render(request,'loja/cadastro.html')
