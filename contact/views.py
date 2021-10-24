from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def contact(request):
    """A view to render the contact page"""

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Message Sent Succesfully!')

            instance = contact_form.save()

            to_email = instance.email
            subject = 'Thank you for contacting Unique Wings'
            message = 'Hi there thank you for contacting with us!....'
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [to_email]
            )
        else:
            messages.error(
                request,
                'Oops, looks like there is an error.\
                    Please ensure the form is valid.')

    contact_form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': contact_form,
    }

    return render(request, template, context)
