from django.urls import path

from .views import Hoge

app_name = 'hoge'

urlpatterns = [
    path('', Hoge.get, name='get'),
]
