from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm
from django.contrib.auth.decorators import login_required


@login_required
def contact_view(request):
    user = request.user
    contacts = Contact.objects.filter(user=user).order_by('-id')
    return render(request, 'contact/contacts.html', {"contacts": contacts})


@login_required
def delete_contact(request, _id):
    contact = get_object_or_404(Contact, pk=_id)
    context = {'contact': contact}

    if request.method == 'GET':
        return render(request, 'contact/contact_confirm_delete.html', context)

    if request.method == "POST":
        contact.delete()
        messages.success(request, 'The post has been deleted successfully.')
        return redirect('contacts')


@login_required
def add_contact(request):
    contact = Contact(user=request.user)

    if request.method == 'GET':
        context = {'form': ContactForm(instance=contact)}
        return render(request, 'contact/edit_new_contact.html', context)

    elif request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been updated successfully.')
            return redirect('contacts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'contact/edit_new_contact.html', {'form': form})


@login_required
def edit_contact(request, _id):
    contact = get_object_or_404(Contact, id=_id)

    if request.method == 'GET':
        context = {'form': ContactForm(instance=contact), 'id': _id}
        return render(request, 'contact/edit_new_contact.html', context)

    elif request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been updated successfully.')
            return redirect('contacts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'contact/edit_new_contact.html', {'form': form})
