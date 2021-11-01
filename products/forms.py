from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = (
            'user',
            'date_posted',
            'product',
        )

        fields = (
            'comment',
            'rate'
        )

        labels = {
            'rate': 'Rate',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'comment': 'Comment',
        }

        # Add placeholders and classes to input fields
        self.fields['comment'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'rate':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].label = False

            self.fields[field].widget.attrs['class'] = (
                'mb-3 rounded-0')
