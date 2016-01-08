from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):

    def setUp(self):
        self.obj = Subscription(
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
