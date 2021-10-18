from django import forms
from .models import BlogPost


class BlogForm(forms.ModelForm):
    """ Create form for blog posts """

    class Meta:
        model = BlogPost
        fields = (
            'title',
            'info',
            'content',
            'image',
            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-teal rounded-0'
