#!/usr/bin/python
# -*- coding: utf-8 -*-


from django.db import models
import datetime

class Categoria(models.Model):
	nome_categoria = models.CharField('Nome', max_length=20)
	descricao_categoria = models.CharField('Descrição', max_length=200) 

	def __unicode__(self):
		return self.nome_categoria
		

class Receita(models.Model):
	nome_receita = models.CharField('Nome', max_length=40)
	descricao_receita = models.CharField('Descrição', max_length=200)
	categoria = models.ForeignKey(Categoria) # será um combobox
	valor_receita = models.FloatField('Valor')
	data_receita = models.DateTimeField('Data de Inserção')

	def __unicode__(self):
		return self.nome_receita

	def publicado_hoje(self):
		return self.data_receita.date() == datetime.date.today()

class Despesa(models.Model):
	nome_despesa = models.CharField('Nome', max_length=40)
	descricao_despesa = models.CharField('Descrição', max_length=200)
	categoria = models.ForeignKey(Categoria) # será um combobox
	valor_despesa = models.FloatField('Valor')
	data_despesa = models.DateTimeField('Data de Inserção')
 
	def __unicode__(self):
		return self.nome_despesa

	def publicado_hoje(self):
		return self.data_despesa.date() == datetime.date.today()
