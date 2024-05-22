from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import ModelFormMixin, DeletionMixin, SingleObjectMixin
from django.urls import reverse
from projects.models import BimProject, BimModel, InfoSheet, Report, ClashTest, ValidationTest

# GLOBAL
class StaffMixin(UserPassesTestMixin):
  """
  this mixin allow projects and BIM models creation only to staff users
  """
  def test_func(self):
    return self.request.user.is_staff

# ORGANIZATION APP
class OrganizationCreateUpdateSuccessUrlMixin(ModelFormMixin):
  def get_success_url(self):
    return reverse('organization_settings')
  
class OrganizationDeleteSuccessUrlMixin(DeletionMixin):
  def get_success_url(self):
    return reverse('organization_settings')


# PROJECTS APP
class BimProjectObjectMixin(SingleObjectMixin):
  model = BimProject

class BimModelObjectMixin(SingleObjectMixin):
  model = BimModel

class InfoSheetObjectMixin(SingleObjectMixin):
  model = InfoSheet

class ReportObjectMixin(SingleObjectMixin):
  model = Report

class ClashTestObjectMixin(SingleObjectMixin):
  model = ClashTest

class ValidationTestObjectMixin(SingleObjectMixin):
  model = ValidationTest