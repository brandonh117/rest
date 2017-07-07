from django.db import models

# Create your models here.
class Persona(models.Model):
	cedulaPer = models.CharField(primary_key=True,max_length=15)
	apellidoPer = models.CharField(max_length=20)
	nombrePer = models.CharField(max_length=20)

	def __str__(self):
		return '{} {}'.format(self.nombrePer, self.apellidoPer)