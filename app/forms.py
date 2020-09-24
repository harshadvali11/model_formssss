from django import forms
from app.models import *


class Topic_Form(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'  # it will include all the model attributes as form attributes



class Webpage_Form(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'