from django.shortcuts import render
from .forms import ContactForm


# Create your views here.


def contact(request):
    """ A view to create the contact page """
    contact_form = ContactForm(request.POST)

    contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }
    template = 'contact/contact.html'

    return render(request, template, context)
