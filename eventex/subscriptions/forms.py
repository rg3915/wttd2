from django import forms
from django.core.exceptions import ValidationError
from localflavor.br.forms import BRCPFField
from eventex.subscriptions.models import Subscription
from eventex.subscriptions.validators import validate_cpf


class SubscriptionForm(forms.ModelForm):
    cpf = BRCPFField(label='CPF', max_length=15)

    class Meta:
        model = Subscription
        fields = ['name', 'cpf', 'email', 'phone']

    def clean_name(self):
        name = self.cleaned_data['name']
        prepositions = ['da', 'de', 'di', 'do', 'du']
        words = list(map(lambda w: w.capitalize()
                         if not w in prepositions else w, name.split()))
        return ' '.join(words)

    def clean_cpf(self):
        return self.cleaned_data['cpf'].replace('.', '').replace('-', '') if self.cleaned_data['cpf'] else self.cleaned_data['cpf']

    def clean(self):
        self.cleaned_data = super().clean()

        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou telefone.')

        return self.cleaned_data
