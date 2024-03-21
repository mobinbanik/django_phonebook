from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact


def say_hello(request):
    return HttpResponse(f"Hello {request.user}")


def contact_view(request):
    user = request.user
    contacts = Contact.objects.filter(user=user).values()
    return render(request, 'contact/contacts.html', {"contacts": contacts})


def delete_contact(request):
    pass


def add_contact(request):
    pass


def edit_contact(request):
    pass
