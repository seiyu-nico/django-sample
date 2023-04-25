from django.urls import path

from .views import Foo

app_name = 'foo'

urlpatterns = [
    path('', Foo.get, name='get'),
]
