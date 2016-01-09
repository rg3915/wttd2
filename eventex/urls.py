from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'', include('eventex.core.urls', namespace='core')),
    url(r'^inscricao/', include('eventex.subscriptions.urls', namespace='subscriptions')),
    url(r'^admin/', admin.site.urls),
]
