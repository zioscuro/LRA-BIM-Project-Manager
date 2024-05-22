from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import ModelFormMixin, DeletionMixin
from django.urls import reverse

class StaffMixin(UserPassesTestMixin):
  """
  this mixin allow projects and BIM models creation only to staff users
  """

  def test_func(self):
    return self.request.user.is_staff
  
class OrganizationCreateUpdateSuccessUrlMixin(ModelFormMixin):
  def get_success_url(self):
    return reverse('organization_settings')
  
class OrganizationDeleteSuccessUrlMixin(DeletionMixin):
  def get_success_url(self):
    return reverse('organization_settings')
