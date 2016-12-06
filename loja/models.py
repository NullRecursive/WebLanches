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


class Produto(models.Model):
	nome = models.CharField(
		max_length = 250, 
		primary_key = True
	)
	preco = models.FloatField()
	descricao = models.TextField(blank = True)
	imagem = models.ImageField(upload_to = 'loja/static/product_images')
	em_Falta = models.BooleanField()

	PRODUTOS =  (('hamburguer',u'Hambuguer'), 
			('bebida',u'Bebida'), 
			('pastel',u'Pastel'), 
			('pizzas', u'Pizzas'))


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
		on_delete = models.CASCADE,
		default = 0,
	)

	quantidade = models.IntegerField(default = 0)


class Pedido(models.Model):
	usuario = models.ForeignKey('auth.User')

	data_do_pedido = models.DateTimeField(default = timezone.now)

	# Em Andamento quando ainda esta na fase de insercao
	# Concluido quando o cliente cncluir suas escolhas
	# Finalizado quando o atendente concluir a producao
	# Em Entrega quando esta a caminho do solicitante
	# Encerrado foi entregue e encerrado 
	ESTADO_PEDIDO = (('em_andamento', 'Em Andamento'), 
					('concluido', 'Concluido'),
					('finalizado', 'Finalizado'), 
					('em_entrega', 'Em Entrega'), 
					('encerrado', 'Encerrado'))


	estado_do_pedido = models.CharField(
		max_length = 12,
		choices = ESTADO_PEDIDO, 
		default = ESTADO_PEDIDO[0])
	
	def concluir_pedido(self):
		self.data_do_pedido = timezone.now()
		self.estado_do_pedido = ESTADO_PEDIDO[1]
		self.save

	
	def finalizar_pedido(self):
		self.estado_do_pedido = ESTADO_PEDIDO[2]
		self.save

	def entregar_pedido(self):
		self.estado_do_pedido = ESTADO_PEDIDO[3]
		self.save
	
	def encerrar_pedido(self):
		self.estado_do_pedido = ESTADO_PEDIDO[4]
		self.save

	def __str__(self):
		return '%s %d' % (self.usuario, self.pk)

	


