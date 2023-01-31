from django import forms
from.models import ContactUS
from.models import Blog_model

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUS
        fields = '__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog_model
        fields = '__all__'
