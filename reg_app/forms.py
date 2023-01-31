from captcha.fields import ReCaptchaField
from django import forms

class MyForm(forms.Form):
    captcha = ReCaptchaField()