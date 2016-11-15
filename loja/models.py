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






