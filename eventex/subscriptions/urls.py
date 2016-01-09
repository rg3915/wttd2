from django.conf.urls import url
import eventex.subscriptions.views as s

urlpatterns = [
    url(r'^$', s.new, name='new'),
    url(r'^(\d+)/$', s.detail, name='detail'),
]
