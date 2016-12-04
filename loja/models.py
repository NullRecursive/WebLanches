from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
	telefone = models.CharField(max_length = 20)
	cpf = models.CharField(max_length = 20)
	endereco = models.CharField(max_length = 250)
	cep = models.CharField(max_length = 8)
	
	def save(self,*args,**kwargs):
		self.set_password(self.password)
		User.save(self)

class Produto(models.Model):
	nome = models.CharField(max_length = 250, primary_key = True)
	preco = models.FloatField()
	descricao = models.TextField(blank = True)
	imagem = models.ImageField(upload_to = 'loja/static/product_images') #falta corrigir bug no GET
	em_Falta = models.BooleanField()

	def __str__(self):
		return self.nome

class Item(models.Model):
	id_produto = models.ForeignKey(
		'Produto',
		on_delete = models.CASCADE,
	)
	id_pedido = models.ForeignKey(
		'Pedido',
		on_delete=models.CASCADE,
	)

	quantidade = models.IntegerField(default = 0)

	

class Pedido(models.Model):
	usuario = models.ForeignKey(
		'Usuario',
		on_delete = models.CASCADE,
	)

	data_do_pedido = models.DateTimeField()

