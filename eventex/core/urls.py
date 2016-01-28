from django.conf.urls import include, url
from eventex.core.views import home, bubble, sendemail

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^bubble/$', bubble, name='bubble'),
    url(r'^email/$', sendemail, name='sendemail'),
]
