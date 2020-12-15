from django import forms
from .models import *

class catform(forms.ModelForm):
    class Meta:
        model = Cats
        fields = ['name', 'petname', 'cat_img', 'cat_drawing', 'addr1', 'addr2', 'city', 'state', 'itn', 'postcode' , 'contact', 'venmo', 'show']
