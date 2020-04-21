from django import forms
from .models import Contact , Subscribe


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [ 'Name', 'Email' , 'Subject' , 'Message']

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields  = [ 'email','status', 'created_date' , 'updated_date' ]

