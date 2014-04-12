from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

# Create your tests here.
from django.test.client import Client

#testing de urls
from principal import views


class Testing(TestCase):
    """
    Clase para realizar los testings.
    """
    def setUp(self):
        self.user = User.objects.create_user('test', 'carlifer.fernando@gmail.com', 'test')


    def testUsuario(self):
        """
        Test de la url de usuario.
        """
        response = self.client.get("/usuario")
        print 'hecho'
        print self.assertEqual(response.status_code, 301)


    def testUsuarioComparacion(self):
        """
        Testing de comparacion de usuario test
        """
        user1 = User.objects.get(username='test')
        self.assertEqual(self.user.email, user1.email)


    def testLogin(self):
        """
        Testeo de Login
        """
        self.assertTrue(self.client.login(username='test', password='test'))


    def tearDown(self):
        self.user.delete()