from django.conf.urls import url
from django.contrib import admin
import eventex.core.views as v
import eventex.subscriptions.views as s

urlpatterns = [
    url(r'^$', v.home, name='home'),
    url(r'^bubble/$', v.bubble, name='bubble'),
    url(r'^email/$', v.sendemail, name='sendemail'),

    url(r'^inscricao/$', s.subscribe, name='subscribe'),
    url(r'^inscricao/(\d+)/$', s.detail, name='detail'),

    url(r'^admin/', admin.site.urls),
]
