from django.utils import unittest
from django.test.client import Client
from sgfd.login.models import Usuario

class UsuarioTestCase(unittest.TestCase):
    
    client = Client()
    
    usuario1 = Usuario()
    
    usuario2 = Usuario()
    
    def test_usuario_criacao(self):
        self.usuario1 = Usuario.objects.create(nome="Usuario 1", senha="1111", email="usuario1@email.com", tipo="internauta", data_entrada="2011-11-01 00:00")
        self.usuario2 = Usuario.objects.create(nome="Usuario 2", senha="2222", email="usuario2@email.com", tipo="internauta", data_entrada="2011-11-01 00:00")
            
    def test_loading_usuario_lista(self):
        response = self.client.get('/admin/auth/user/')
        self.assertEqual(response.status_code, 200)
    
    def test_loading_usuario_add(self):
        response = self.client.get('/admin/auth/user/add/')
        self.assertEqual(response.status_code, 200)
    

    def test_loading_usuario_update(self):
        response = self.client.get('/admin/auth/user/1/')
        self.assertEqual(response.status_code, 200)

    
    def test_usuario_add(self):
        """
        Testando se ao adicionar um usuario os dados sao preenchidos corretamente.
        """
        self.usuario1 = Usuario.objects.create(nome="Usuario 1", senha="1111", email="usuario1@email.com", tipo="internauta", data_entrada="2011-11-01 00:00")
        self.assertEqual(self.usuario1.nome, "Usuario 1")
        
    
    def test_usuario_update(self):
        """
        Testando se ao alterar um usuario os dados sao preenchidos corretamente.
        """
        self.usuario1 = Usuario.objects.create(nome="Usuario 1", senha="1111", email="usuario1@email.com", tipo="internauta", data_entrada="2011-11-01 00:00")
        self.assertEqual(self.usuario1.nome, "Usuario 1")
        
        self.usuario1.nome = "Usuario Novo"
        self.assertNotEqual(self.usuario1.nome, "Usuario 1")

    

