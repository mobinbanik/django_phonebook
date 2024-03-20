from django.urls import path
from .views import say_hello

urlpatterns = [
    path('', say_hello, name='hello'),
]