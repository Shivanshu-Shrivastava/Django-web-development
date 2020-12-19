from django import forms
from .models import email
class create_form(forms.Form):
    Name=forms.CharField(label="Name",max_length=100)
class form_maping_with_model(forms.ModelForm):
    class Meta:
        model=email
        fields=['Email',
                'password'
                ]
