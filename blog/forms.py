from django import forms
from django.core.exceptions import ValidationError

from .models import *


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()  # self.cleaned_data.get['slug']

        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"!')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('This slug already exists: "{}"'.format(new_slug))
        return new_slug


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'row': '3'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()  # self.cleaned_data.get['slug']
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"!')
        return new_slug
