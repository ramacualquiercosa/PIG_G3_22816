from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Thread
# Create your tests here.

class ThreadTestCase(TestCase):
    def setUp(self):
        self.user1 =  User.objects.create_user('user1', None, 'test1234')
        self.user2 =  User.objects.create_user('user2', None, 'test1234')

        self.thread = Thread.objects.create()

    def test_add_users_to_thread(self):#comprueba la creacion de usuarios y su cantidad
        self.thread.users.add(self.user1, self.user2)
        self.assertEqual(len(self.thread.users.all()), 2)

    def test_filter_thread_by_user(self):#recupera y comprueba un hilo creado
        self.thread.users.add(self.user1, self.user2)
        threads = Thread.objects.filter(users = self.user1).filter(user = self.user1)#recupera el hilo a partir de los usuarios especificados
        self.assertEqual(self.thread, threads[0])

   
    def test_filter_non_existent_thread(self):
        threads = Thread.objects.filter(users = self.user1).filter(users = self.user1)
        self.assertEqual(len(threads), 0)

    def test_add_messages_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        message1= Message.objects.create(users=self.user1, content="Hola Juan")
        message2= Message.objects.create(users=self.user1, content="Hola Pepe")
        self.thread.messages.add(message1, message2)
        self.assertEqual(len(self.thread.messages.all()), 2)

    