from django.conf.urls import url
import eventex.subscriptions.views as s

urlpatterns = [
    url(r'^$', s.new, name='new'),
    url(r'^(\d+)/$', s.detail, name='detail'),
    url(r'^json/$', s.paid_list_json, name='paid_list_json'),
    url(r'^graphic/$', s.graphic, name='graphic'),
]
