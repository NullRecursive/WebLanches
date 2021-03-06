from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image

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

	ativo = models.BooleanField(default = True)

	def get_produto():
		produto = Produto.objects.filter()

	@classmethod
	def total(self, id_pedido):
		itens = Item.objects.filter(id_pedido = id_pedido)
		value = 0.0
		for item in itens:
			 produto = Produto.objects.get(nome = item.id_produto)
			 value += (produto.preco*item.quantidade)
		return value

	def addQuantidade(self, quantidade):
		self.quantidade += quantidade

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
		default = ESTADO_PEDIDO[0][0])


	def __str__(self):
		return '%s %d' % (self.usuario, self.pk)

	def save(self, force_insert=False, force_update=False):
		self.data_do_pedido = timezone.now()
		super(Pedido, self).save(force_insert, force_update)


# SIGNAL
@receiver(post_save, sender = Pedido)
def create_info(sender, instance, created, **kwargs):
    print ('O Pedido foi salvo')


post_save.connect(create_info, sender = Pedido)
