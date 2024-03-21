from django.urls import path
from .views import *

urlpatterns = [
    path('', contact_view, name='contacts'),
    path('new-contacts/', add_contact, name='new_contact'),
    path('edit-contact/', edit_contact, name='edit_contact'),
    path('delete-contact/', delete_contact, name='delete_contact'),
]
