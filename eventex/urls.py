from django.conf.urls import url
from django.contrib import admin
import eventex.core.views as v

urlpatterns = [
    url(r'^$', v.home, name='home'),
    url(r'^email/$', v.sendemail, name='sendemail'),
    url(r'^email/subscribe$', v.subscribe, name='subscribe'),
    url(r'^admin/', admin.site.urls),
]
