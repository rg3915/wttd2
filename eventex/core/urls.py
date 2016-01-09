from django.conf.urls import include, url
import eventex.core.views as v

urlpatterns = [
    url(r'^$', v.home, name='home'),
    url(r'^bubble/$', v.bubble, name='bubble'),
    url(r'^email/$', v.sendemail, name='sendemail'),
]
