from django import forms
from.models import Contact

class Contact_Form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'recaptcha']
