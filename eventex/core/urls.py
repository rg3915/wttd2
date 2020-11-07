from django.urls import include, path
from eventex.core.views import home, bubble, sendemail


app_name = 'core'


urlpatterns = [
    path('', home, name='home'),
    path('bubble/', bubble, name='bubble'),
    path('email/', sendemail, name='sendemail'),
]
