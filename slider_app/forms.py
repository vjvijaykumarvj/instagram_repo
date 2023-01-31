from.models import Washing_Payment
from django import forms

class Washing_payment_Forms(forms.ModelForm):
    class Meta:
        model = Washing_Payment
        fields = '__all__'
