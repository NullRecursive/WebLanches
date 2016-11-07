from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
	telefone = models.CharField(max_length=20)
	cpf = models.CharField(max_length=20)


	def setTelefone(self,telefone):
		self.telefone = telefone

	def setCPF(self,cpf):
		self.cpf = cpf

	def save(self,*args,**kwargs):
		self.set_password(self.password)
		User.save(self);
	


