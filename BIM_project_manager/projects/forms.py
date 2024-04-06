from django import forms
from .models import BimModel, InfoSheet, Report, ClashTest, ValidationTest

# class AddBimModelForm(forms.ModelForm):  
#   class Meta:
#     model = BimModel
#     fields = ['name', 'discipline', 'designer', 'authoringSoftware', 'lodReference']

# class AddInfoSheetForm(forms.ModelForm):
#   class Meta:
#     model = InfoSheet
#     fields = ['name', 'description']

# class AddReportForm(forms.ModelForm):
#   class Meta:
#     model = Report
#     fields = ['name', 'description']

class AddClashTestForm(forms.ModelForm):
  class Meta:
    model = ClashTest
    fields = ['comments', 'clash_new', 'clash_active', 'clash_reviewed', 'clash_approved', 'clash_resolved']

class AddValidationTestForm(forms.ModelForm):
  class Meta:
    model = ValidationTest
    fields = ['comments', 'specification', 'issues']
