from datetime import datetime
from django.test import TestCase
from django.db import IntegrityError
from django.utils.crypto import get_random_string
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):

    def setUp(self):
        self.obj = Subscription(
            uuid='932909e8-79de-4163-9134-acbd56ced2a7',
            name='Regis da Silva',
            cpf='12345678901',
            email='regis@example.com',
            phone='11 91234-5678')
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        ''' Subscription must have an auto created_at attr. '''
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Regis da Silva', str(self.obj))

    def test_len_uuid(self):
        self.assertEqual(len(self.obj.uuid), 36)

    def test_uuid_is_str(self):
        self.assertIs(type(self.obj.uuid), str)


class SubscriptionUniqueTest(TestCase):

    def setUp(self):
        # Create a first entry to force the collision.
        Subscription.objects.create(
            uuid='932909e8-79de-4163-9134-acbd56ced2a7',
            name='Regis da Silva',
            cpf='12345678901',
            email='regis@example.com',
            phone='11 91234-5678')

    def test_uuid_unique(self):
        'UUID must be unique'
        s = Subscription(
            uuid='932909e8-79de-4163-9134-acbd56ced2a7',
            name='Regis da Silva',
            cpf='12345678901',
            email='regis@example.com',
            phone='11 91234-5678')
        self.assertRaises(IntegrityError, s.save)
