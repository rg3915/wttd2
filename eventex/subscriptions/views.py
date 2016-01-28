import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.views.generic import DetailView
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.mixins import EmailCreateView
from eventex.subscriptions.models import Subscription


new = EmailCreateView.as_view(model=Subscription,
                              form_class=SubscriptionForm,
                              email_subject='Confirmação de inscrição')

detail = DetailView.as_view(model=Subscription)


def count_paid(paid=True):
    return Subscription.objects.filter(paid=paid).count()


def get_data(paid_yes, paid_no):
    data = [{'label': 'Sim', 'value': paid_yes},
            {'label': 'Não', 'value': paid_no},
            ]
    return data


def paid_list_json(request):
    ''' JSON used to generate the graphic '''
    ''' Percent of paid '''
    paid = count_paid()
    total = Subscription.objects.count()
    paid_yes = int(paid * 100 / total)
    paid_no = 100 - paid_yes
    resp = JsonResponse(get_data(paid_yes, paid_no), safe=False)
    return HttpResponse(resp.content)


def paid_column_json(request):
    ''' JSON used to generate the graphic '''
    ''' Quantity of paid '''
    paid_yes = count_paid()
    paid_no = count_paid(paid=False)
    resp = JsonResponse(get_data(paid_yes, paid_no), safe=False)
    return HttpResponse(resp.content)


@login_required
def graphic(request):
    return render(request, 'subscriptions/graphic.html')
