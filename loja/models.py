from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
	telefone = models.CharField(max_length=20)
	cpf = models.CharField(max_length=20)
	endereco = models.CharField(max_length=250)
	cep = models.CharField(max_length=8)
<<<<<<< HEAD


	def save(self):
=======
	
	def save(self,*args,**kwargs):
>>>>>>> 7898973c2462a19b28f4899f048450be2aa89066
		self.set_password(self.password)
		User.save(self)






