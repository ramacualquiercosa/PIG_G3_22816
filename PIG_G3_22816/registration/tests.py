from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User
# Create your tests here.

#Permite testear si se crea un usuario vinculado a una instancia, sirve para testear el codigo que crea usuarios e instancias
class  ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test','test@test.com','test1234')

    def test_profile_exists(self):
        exists= Profile.objects.filter(user__username='test').exists()
        self.assertEqual(exists, True)