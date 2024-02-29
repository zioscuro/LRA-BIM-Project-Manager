from django import forms
from .models import BimModel, InfoSheet

class AddBimModelForm(forms.ModelForm):  
  class Meta:
    model = BimModel
    fields = ['name', 'discipline', 'designer']

class AddInfoSheetForm(forms.ModelForm):
  class Meta:
    model = InfoSheet
    fields = ['name', 'description']
