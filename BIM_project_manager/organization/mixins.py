from django.views.generic.edit import ModelFormMixin, DeletionMixin, SingleObjectMixin
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from core.mixins import StaffMixin
from organization.models import ProjectPhase, Discipline, AuthoringSoftware, LodReference, BimSpecification, BimExpert

# class OrganizationCreateUpdateSuccessUrlMixin(ModelFormMixin):
#   def get_success_url(self):
#     return reverse('organization_settings')
  
# class OrganizationDeleteSuccessUrlMixin(DeletionMixin):
#   def get_success_url(self):
#     return reverse('organization_settings')


class ProjectPhaseViewMixin(StaffMixin, SingleObjectMixin):
  model = ProjectPhase

class DisciplineViewMixin(StaffMixin, SingleObjectMixin):
  model = Discipline

class AuthoringSoftwareViewMixin(StaffMixin, SingleObjectMixin):
  model = AuthoringSoftware

class LodReferenceViewMixin(StaffMixin, SingleObjectMixin):
  model = LodReference

class BimSpecificationViewMixin(StaffMixin, SingleObjectMixin):
  model = BimSpecification

class BimExpertViewMixin(StaffMixin, SingleObjectMixin):
  model = BimExpert

class OrganizationCreateView(CreateView):
  def get_success_url(self):
    return reverse('organization_settings')

class OrganizationUpdateView(UpdateView):  
  def get_success_url(self):
    return reverse('organization_settings')
  
class OrganizationDeleteView(DeleteView):
  def get_success_url(self):
    return reverse('organization_settings')