from django import forms
from django.core.exceptions import ValidationError
from localflavor.br.forms import BRCPFField, BRPhoneNumberField


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números.', None)

    if len(value) != 11:
        raise ValidationError('CPF deve ter 11 números.', 'min_length')


class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = BRCPFField(label='CPF', validators=[validate_cpf])
    email = forms.EmailField(label='Email', required=False)
    phone = BRPhoneNumberField(label='Telefone', required=False)

    def clean_name(self):
        name = self.cleaned_data['name']
        prepositions = ['da', 'de', 'di', 'do', 'du']
        words = list(map(lambda w: w.capitalize()
                         if not w in prepositions else w, name.split()))
        return ' '.join(words)

    def clean(self):
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou telefone.')
        return self.cleaned_data
