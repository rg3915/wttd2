from django import forms
from django.core.exceptions import ValidationError
from localflavor.br.forms import BRCPFField, BRPhoneNumberField
from eventex.subscriptions.models import Subscription
from eventex.subscriptions.validators import validate_cpf


class SubscriptionFormOld(forms.Form):
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
        cpf = self.cleaned_data['cpf']
        cpf = cpf[:3] + cpf[4:7] + cpf[8:11] + cpf[12:]
        return ''.join(cpf)

    def clean(self):
        self.cleaned_data = super().clean()

        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou telefone.')

        return self.cleaned_data
