from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
	telefone = models.CharField(max_length=20)
	cpf = models.CharField(max_length=20)
	endereco = models.CharField(max_length=250)
	cep = models.CharField(max_length=8)
	
	def save(self,*args,**kwargs):
		self.set_password(self.password)
		User.save(self)



class Produto(models.Model):
	nome = models.CharField(max_length=250,primary_key=True)
	preco = models.FloatField()
	descricao = models.TextField(blank = True)
	imagem = models.ImageField(upload_to='loja/static/product_images') #falta corrigir bug no GET
	em_Falta = models.BooleanField()

	def __str__(self):
		return self.nome