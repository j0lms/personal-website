from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name' , 'email' , 'message', 'date_submitted')

# Register your models here.
