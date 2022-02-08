from django import forms
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit#, Field


class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_method = 'post'
        self.helper.form_action = 'contact'

        self.helper.add_input(Submit('submit', _('Submit')))

    name = forms.CharField(label=_('Name'), max_length=80)
    email = forms.EmailField(label=_('Email'), max_length=254)
    message = forms.CharField(label=_('Body'), max_length=254, widget=forms.Textarea)