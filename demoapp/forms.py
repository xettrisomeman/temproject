from django import forms 

from .models import Home_carousel_one

class form_carousel_one(forms.ModelForm):

    class Meta:
        model = Home_carousel_one
        fields = ['img']
