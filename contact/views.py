from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Newsletter
from .forms import ContactForm, NewsletterForm


def contact(request):
    """A view to render the contact page"""

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Message Sent Succesfully!')

            instance = contact_form.save()

            to_email = instance.email
            subject = render_to_string(
                'contact/emails/email_subject.txt',
                {'instance': instance})
            message = render_to_string(
                'contact/emails/email_message.txt',
                {'instance': instance,
                 'contact_email': settings.DEFAULT_FROM_EMAIL})
            # send an email
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [to_email]
            )
        else:
            messages.error(
                request,
                'Looks like there is an error.\
                    Please ensure the form is valid.')

    contact_form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': contact_form,
    }

    return render(request, template, context)


def newsletter_signup(request):

    newsletter_form = NewsletterForm(request.POST or None)
    redirect_url = request.POST.get("redirect_url")

    if newsletter_form.is_valid():
        instance = newsletter_form.save(commit=False)
        if (Newsletter.objects.filter(
                email=instance.email).exists()):
            messages.info(request, 'You are already\
                            signed up for our newsletter.')
        else:
            instance.save()
            messages.success(request, 'Thank you!\
                             You are now signed up to our newsletter.')

    return redirect(redirect_url)


def newsletter_unsubscribe(request):

    newsletter_form = NewsletterForm(request.POST or None)

    if newsletter_form.is_valid():
        instance = newsletter_form.save(commit=False)
        if (Newsletter.objects.filter(
                email=instance.email).exists()):
            Newsletter.objects.filter(
                email=instance.email).delete()
            messages.success(request, f'{instance.email}\
                have been removed from subscription.')
        else:
            messages.error(request, 'Sorry! That email address\
                            does not exist in our database.')

    newsletter_form = NewsletterForm()

    template = 'contact/newsletter_unsubscribe.html'
    context = {
        'newsletter_form': newsletter_form,
    }

    return render(request, template, context)
