from django import forms
from .models import RateHistory


class DateInput(forms.DateInput):
    input_type = 'date'


class RateSavingForm(forms.ModelForm):
    ua_rate = forms.DecimalField(max_digits=8, decimal_places=2, min_value=0.01)  # Add validations to rate form field

    class Meta:
        model = RateHistory
        fields = ['ua_rate', 'date']  # Fields to use in form
        widgets = {
            'ua_rate': forms.NumberInput(attrs={'class': 'mb-3 d-inline'}),  # Add attributes to rate field
            'date': DateInput()
        }



