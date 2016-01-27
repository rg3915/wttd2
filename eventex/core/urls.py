from django.conf.urls import include, url
from eventex.core.views import HomeView, bubble, sendemail

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^bubble/$', bubble, name='bubble'),
    url(r'^email/$', sendemail, name='sendemail'),
]
