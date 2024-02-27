from django import forms
from .models import BimModel

class AddBimModelForm(forms.ModelForm):
  
  class Meta:
    model = BimModel
    fields = ['name', 'discipline', 'designer']