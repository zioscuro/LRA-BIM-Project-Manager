from django import forms
from .models import BimModel, Report, ClashTest, ValidationTest
 
class BimModelCreateForm(forms.ModelForm):
  class Meta:
    model = BimModel
    exclude = ('bim_project', 'designer', 'bim_manager', 'bim_coordinator', 'bim_specialist', 'default_coordination', 'default_validation')

class BimModelUpdateForm(forms.ModelForm):
  class Meta:
    model = BimModel
    exclude = ('bim_project', 'default_coordination', 'default_validation')

class ReportForm(forms.ModelForm):
  class Meta:
    model = Report
    exclude = ('info_sheet',)

class ClashTestForm(forms.ModelForm):
  class Meta:
    model = ClashTest
    exclude = ('report',)

class ValidationTestForm(forms.ModelForm):
    class Meta:
      model = ValidationTest
      exclude = ('report',)

class UploadFileForm(forms.Form):
  file = forms.FileField()
