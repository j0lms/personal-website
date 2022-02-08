from django.contrib import messages
from django.views.generic.edit import FormView
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.core.mail import send_mail
# from django.utils import translation

from .forms import ContactForm
from .models import Message



class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        http_header = self.request.META
        send_email(form, http_header)

        message = Message(name=name, email=email, message=message)
        message.save()

        messages.success(self.request, _('Message received'))

        return super().form_valid(form)

#    def form_invalid(self, form):
#        name = form.cleaned_data['name']
#        email = form.cleaned_data['email']
#        message = form.cleaned_data['message']
#        http_header = self.request.META
#        send_email(form, http_header)

#        message = Message(name=name, email=email, message=message)
#        message.save()
#        messages.error(self.request, _('Something went wrong with your submission. Please try again.'))
#        return HttpResponseRedirect('')

def send_email(form_data, http_header):
    try:
        if http_header.get('HTTP_X_REAL_IP'):
            remote_ip = http_header.get('HTTP_X_REAL_IP')
        elif http_header.get('X-FORWARDED-FOR'):
            http_header.get('X-FORWARDED-FOR')
        else:
            remote_ip = 'We were not able to fetch IP Address of client'
    except:
        pass
    form_message = form_data.cleaned_data['message']
    name = form_data.cleaned_data['name']
    try:
        email = form_data.cleaned_data['email']
    except:
        email = 'INVALID EMAIL'
    message = f'''The current message was received from {email} with IP={remote_ip}:
    {form_message}
    '''
    send_mail(name,
        message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.ADMIN_EMAIL],
        fail_silently=False)

# Create your views here.
