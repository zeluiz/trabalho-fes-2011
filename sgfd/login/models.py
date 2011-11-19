#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
import datetime

class Usuario(models.Model):
	nome = models.CharField(max_length=15)
	senha = models.CharField(max_length=12)
	email = models.EmailField()
	tipo = models.CharField(max_length=13)
	data_entrada = models.DateTimeField()
 
	def __unicode__(self):
		return self.nome

	def publicado_hoje(self):
		return self.data_entrada.date() == datetime.date.today()
