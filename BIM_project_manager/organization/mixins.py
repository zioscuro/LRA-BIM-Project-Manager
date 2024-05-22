from django.views.generic.edit import ModelFormMixin, DeletionMixin, SingleObjectMixin
from django.urls import reverse

from organization.models import ProjectPhase, Discipline, AuthoringSoftware, LodReference, BimSpecification, BimExpert

class OrganizationCreateUpdateSuccessUrlMixin(ModelFormMixin):
  def get_success_url(self):
    return reverse('organization_settings')
  
class OrganizationDeleteSuccessUrlMixin(DeletionMixin):
  def get_success_url(self):
    return reverse('organization_settings')
  
class ProjectPhaseObjectMixin(SingleObjectMixin):
  model = ProjectPhase

class DisciplineObjectMixin(SingleObjectMixin):
  model = Discipline

class AuthoringSoftwareObjectMixin(SingleObjectMixin):
  model = AuthoringSoftware

class LodReferenceObjectMixin(SingleObjectMixin):
  model = LodReference

class BimSpecificationObjectMixin(SingleObjectMixin):
  model = BimSpecification

class BimExpertObjectMixin(SingleObjectMixin):
  model = BimExpert

