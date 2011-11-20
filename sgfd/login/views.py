#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from sgfd.login.models import  Usuario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



def home (request):
   if request.method == 'POST':
       usuario = request.POST['login']
       senha = request.POST['senha']
       
       user = authenticate(username=usuario, password=senha)
       
       if user is not None:
           if user.is_active:
               login(request,user)
               return redirect('/perfil')
           else:
               msg = 'Conta desativada!! Favor entrar em contato com administradores do site.'
               return render_to_response('home.html', {'msg': msg}, context_instance=RequestContext(request))
       else:
           msg = 'Usuario/Senha invalidos!'
           return render_to_response('home.html', {'msg': msg}, context_instance=RequestContext(request))
   else:
       return render_to_response('home.html', context_instance=RequestContext(request))
    
def cadastro (request):	
   if request.method == 'POST':
       nome = request.POST['nome']
       email = request.POST['email']
       cpf = request.POST['cpf']
       uf = request.POST['uf']
       cidade = request.POST['cidade']
       endereco = request.POST['endereco']
       login = request.POST['login']
       senha = request.POST['senha']
       tipo = request.POST['tipo']
		
       usuario_django = User.objects.create_user(login,email, senha)
       usuario_django.first_name = nome
       usuario_django.is_staff=True
       usuario_django.is_active=True
       usuario_django.is_superuser=False
       usuario_django.save()
       
       usuario_sgfd = Usuario.objects.create(usuario=usuario_django, nome_completo=nome, senha=senha, email=email, cpf=cpf, tipo=tipo, data_entrada=usuario_django.date_joined)
       usuario_sgfd.save()
       
       msg = u'Operação finalizada com sucesso!!'
       return render_to_response('home.html', {'msg': msg}, context_instance=RequestContext(request))
       
    
   else:
       return render_to_response('cadastro.html', context_instance=RequestContext(request))
		

def perfil (request):
   return render_to_response('perfil.html', context_instance=RequestContext(request))

def sair (request):
   logout(request)
   return redirect('/')    