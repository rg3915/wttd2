from django.conf.urls import url
from django.contrib import admin
import eventex.core.views as v

urlpatterns = [
    url(r'^$', v.home, name='home'),
    url(r'^admin/', admin.site.urls),
]
