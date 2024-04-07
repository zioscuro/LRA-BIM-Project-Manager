from django import forms
from .models import ClashTest, ValidationTest


class AddValidationTestForm(forms.ModelForm):
  class Meta:
    model = ValidationTest
    fields = ['comments', 'specification', 'issues']
