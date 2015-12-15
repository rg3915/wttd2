from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    return render(request, 'index.html')


def subscribe(request):
    if request.method == 'POST':
        from_email = request.POST.get('from_email', '')
        to_email = 'regis.santos.100@gmail.com'
        message = '<html><body><h2>Obrigado por se inscrever no Eventex.</h2><p>Em breve entraremos em contato.</p></body></html>'
        if from_email:
            try:
                # email para mim
                send_mail('Inscrição no Eventex', from_email + ' se inscreveu no Eventex.', from_email,
                          [to_email], fail_silently=False)
                # email para o inscrito
                send_mail('Inscrição no Eventex', message, to_email,
                          [from_email], fail_silently=False, html_message=message)
                print('Email enviado com sucesso.')
            except BadHeaderError:
                return HttpResponse('Cabeçalho inválido.')
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Certifique-se de todos os campos estão inseridos e válidos.')


def sendemail(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        subject = request.POST.get('subject', '')
        from_email = request.POST.get('email', '')
        to_email = 'regis.santos.100@gmail.com'
        message = request.POST.get('message', '')
        html_message_from = '<html><body><p>Mensagem enviada por ' + \
            name + ', ' + from_email + '</p><p>' + message + '</p></body></html>'
        html_message = '<html><body><h2>Você enviou uma mensagem para Eventex.</h2><p><b>Sua Mensagem:</b></p><p>' + \
            message + '</p></br></br><p><b>Resposta:</b></p><p>Bem-vindo ao Eventex. Em breve entraremos em contato.</p></body></html>'
        if subject and message and from_email:
            try:
                # email para mim
                send_mail(subject, message, from_email,
                          [to_email], fail_silently=False, html_message=html_message_from)
                # email para quem enviou a mensagem
                send_mail(subject, message, to_email,
                          [from_email], fail_silently=False, html_message=html_message)
                print('Email enviado com sucesso.')
            except BadHeaderError:
                return HttpResponse('Cabeçalho inválido.')
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Certifique-se de todos os campos estão inseridos e válidos.')
