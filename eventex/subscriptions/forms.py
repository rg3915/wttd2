from django import forms


class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', max_length=11)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Telefone')
