from django.forms import ModelForm
from .models import BimModel, Report, ClashTest, ValidationTest
 
class BimModelCreateForm(ModelForm):
  class Meta:
    model = BimModel
    exclude = ('bim_project', 'designer', 'bim_manager', 'bim_coordinator', 'bim_specialist', 'default_coordination', 'default_validation')

class BimModelUpdateForm(ModelForm):
  class Meta:
    model = BimModel
    exclude = ('bim_project', 'default_coordination', 'default_validation')

class ReportForm(ModelForm):
  class Meta:
    model = Report
    exclude = ('info_sheet',)

class ClashTestForm(ModelForm):
  class Meta:
    model = ClashTest
    exclude = ('report',)

class ValidationTestForm(ModelForm):
  class Meta:
    model = ValidationTest
    exclude = ('report',)