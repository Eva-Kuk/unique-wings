from django import forms
from .widgets import CustomClearableFileInput
from .models import BlogPost, BlogComment


class BlogForm(forms.ModelForm):
    """ Create BlogForm for blog posts """

    class Meta:
        model = BlogPost
        fields = (
            'title',
            'info',
            'content',
            'image',
            )

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class CommentForm(forms.ModelForm):
    """ Create CommentForm for blog posts """

    class Meta:
        model = BlogComment
        fields = (
            'comment',
            )
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'comment': 'Comment',
        }

        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False
