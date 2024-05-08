from django.forms import ModelForm
from .models import BimModel
 
class BimModelCreateForm(ModelForm):
  class Meta:
    model = BimModel
    exclude = ('bim_project', 'designer', 'bim_manager', 'bim_coordinator', 'bim_specialist', 'default_coordination', 'default_validation')

class BimModelUpdateForm(ModelForm):
  class Meta:
    model = BimModel
    exclude = ('bim_project', 'default_coordination', 'default_validation')