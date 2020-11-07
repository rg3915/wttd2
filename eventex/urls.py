from django.urls import include, path
from django.contrib import admin

from eventex.core.views import speaker_detail, talk_list

urlpatterns = [
    path('', include('eventex.core.urls', namespace='core')),
    path('inscricao/', include('eventex.subscriptions.urls', namespace='subscriptions')),
    path('palestras/', talk_list, name='talk_list'),
    path('palestrantes/<slug>/', speaker_detail, name='speaker_detail'),
    path('admin/', admin.site.urls),
]
