from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(User):
	telefone = models.CharField(max_length=20)
	cpf = models.CharField(max_length=20)

	def __init__(self):
		self.is_superuser = False;
		self.is_staff = False;

	def setTelefone(self,telefone):
		self.telefone = telefone

	def setCPF(self,cpf):
		self.cpf = cpf
	
	def publish(self):
		self.save() 

