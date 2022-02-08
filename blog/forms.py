from .models import Comment
from django import forms
from django.utils.translation import gettext_lazy as _


class CommentForm(forms.ModelForm):
    class Meta:
        labels = {
            'name': _('Name'),
            'email': _('Email'),
            'body': _('Body'),
        }
        model = Comment
        fields = ('name', 'email', 'body')
