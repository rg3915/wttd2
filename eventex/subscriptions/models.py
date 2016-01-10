from django.db import models


class Subscription(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11)
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone', max_length=20)
    paid = models.BooleanField('pago', default=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'inscrição'
        verbose_name_plural = 'inscrições'

    def __str__(self):
        return self.name
