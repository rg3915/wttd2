# -*- coding: utf-8 -*-
from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribeEmail(TestCase):

    def setUp(self):
        data = dict(
            name='Regis da Silva',
            cpf='71124336656',
            email='regis@example.com',
            phone='11-91234-5678',
        )
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'regis@example.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Regis da Silva',
            '71124336656',
            'regis@example.com',
            '11-91234-5678',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
