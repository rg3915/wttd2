import json
from django.conf import settings
from django.contrib import messages
from django.core import mail, serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, resolve_url as r
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect, Http404
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form': form})

    subscription = form.save()

    # Send subscription email
    _send_mail('Confirmação de inscrição',
               settings.DEFAULT_FROM_EMAIL,
               subscription.email,
               'subscriptions/subscription_email.txt',
               {'subscription': subscription})

    return HttpResponseRedirect(r('subscriptions:detail', subscription.pk))


def detail(request, pk):
    try:
        subscription = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        raise Http404

    return render(request, 'subscriptions/subscription_detail.html', {'subscription': subscription})


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])


def paid_list_json(request):
    ''' JSON used to generate the graphic '''
    ''' percent of paid '''
    paid = Subscription.objects.filter(paid=True).count()
    total = Subscription.objects.count()
    paid_yes = int(paid * 100 / total)
    paid_no = 100 - paid_yes
    data = [{'label': 'Sim', 'value': paid_yes},
            {'label': 'Não', 'value': paid_no},
            ]

    s = json.dumps(data, cls=DjangoJSONEncoder)
    # s = serializers.serialize('json', data)
    return HttpResponse(s)


def graphic(request):
    return render(request, 'subscriptions/graphic.html')
