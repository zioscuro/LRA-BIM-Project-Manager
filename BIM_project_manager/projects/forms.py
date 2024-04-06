from django import forms
from .models import ClashTest, ValidationTest

class AddClashTestForm(forms.ModelForm):
  class Meta:
    model = ClashTest
    fields = ['comments', 'clash_new', 'clash_active', 'clash_reviewed', 'clash_approved', 'clash_resolved']

class AddValidationTestForm(forms.ModelForm):
  class Meta:
    model = ValidationTest
    fields = ['comments', 'specification', 'issues']
