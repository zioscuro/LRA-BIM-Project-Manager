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

# MULTIPLE UPLOAD FORM
class MultipleFileInput(forms.ClearableFileInput):
  allow_multiple_selected = True

class MultipleFileField(forms.FileField):
  def __init__(self, *args, **kwargs):
    kwargs.setdefault("widget", MultipleFileInput())
    super().__init__(*args, **kwargs)

  def clean(self, data, initial=None):
    single_file_clean = super().clean
    if isinstance(data, (list, tuple)):
      result = [single_file_clean(d, initial) for d in data]
    else:
      result = [single_file_clean(data, initial)]
    return result

class MultipleUploadFileForm(forms.Form):
  file_field = MultipleFileField()
