from django.urls import path
import eventex.subscriptions.views as s


app_name = 'subscriptions'


urlpatterns = [
    path('', s.new, name='new'),
    path('<int:id>/', s.detail, name='detail'),
    path('json/donut/', s.paid_list_json, name='paid_list_json'),
    path('json/column/', s.paid_column_json, name='paid_column_json'),
    path('graphic/', s.graphic, name='graphic'),
]
