#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
import datetime
from django.contrib.auth.models import User

class Usuario(models.Model):
    usuario = models.OneToOneField(User)
    nome_completo = models.CharField('Nome Completo', max_length=15)
    senha = models.CharField(max_length=12)
    email = models.EmailField()
    cpf = models.CharField(max_length=15)
    
    TIPO_CHOICES = (
           ('PG', 'Assinante'),
           ('NPG', 'Gratuito'),
       )
    tipo = models.CharField(max_length=5, choices=TIPO_CHOICES)
    
    data_entrada = models.DateTimeField()
 
    def __unicode__(self):
        return self.nome_completo

	def publicado_hoje(self):
		return self.data_entrada.date() == datetime.date.today()
