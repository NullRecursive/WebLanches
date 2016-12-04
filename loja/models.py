from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Usuario(User):
	telefone = models.CharField(max_length = 20)
	cpf = models.CharField(max_length = 20)
	endereco = models.CharField(max_length = 250)
	cep = models.CharField(max_length = 8)
	
	def save(self,*args,**kwargs):
		self.set_password(self.password)
		User.save(self)

PRODUTOS =  (('hamburguer',u'Hambuguer'), 
			('bebida',u'Bebida'), 
			('pastel',u'Pastel'), 
			('pizzas', u'Pizzas'))

class Produto(models.Model):
	nome = models.CharField(
		max_length = 250, 
		primary_key = True
	)
	preco = models.FloatField()
	descricao = models.TextField(blank = True)
	imagem = models.ImageField(upload_to = 'loja/static/product_images')
	em_Falta = models.BooleanField()
	categoria = models.CharField(
		max_length = 10,
		choices = PRODUTOS,
		default = PRODUTOS[0]
	)

	def __str__(self):
		return self.nome

class Item(models.Model):
	id_produto = models.ForeignKey(
		'Produto',
		on_delete = models.CASCADE,
		default = 0,
	)
	id_pedido = models.ForeignKey(
		'Pedido',
		on_delete=models.CASCADE,
		default = 0,
	)

	quantidade = models.IntegerField(default = 0)

	

class Pedido(models.Model):
	usuario = models.ForeignKey('auth.User')

	data_do_pedido = models.DateTimeField(default = timezone.now)
	concluido = models.BooleanField(default = False)

	def salvar_pedido(self):
		self.data_do_pedido = timezone.now()
		self.save

	def __str__(self):
		return '%s %d' % (self.usuario, self.pk)

	


