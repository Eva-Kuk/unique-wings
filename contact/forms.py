from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Creates Contact form"""

    class Meta:
        model = Contact
        fields = (
            'full_name',
            'email',
            'subject',
            'message',
            )


def __init__(self, *args, **kwargs):
    """
    Add placeholders and classes, remove auto-generated
    labels and set autofocus on first field
    """
    super().__init__(*args, **kwargs)
    placeholders = {
        'full_name': 'Full Name',
        'email': 'Email',
        'subject': 'Subject',
        'message': 'Message',
    }

    self.fields['full_name'].widget.attrs['autofocus'] = True
    for field in self.fields:
        if field != 'subject':
            placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class'] = 'stripe-style-input'
        self.fields[field].label = False
