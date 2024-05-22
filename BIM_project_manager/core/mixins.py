from django.contrib.auth.mixins import UserPassesTestMixin

class StaffMixin(UserPassesTestMixin):
  """
  this mixin allow projects and BIM models creation only to staff users
  """
  def test_func(self):
    return self.request.user.is_staff

# ORGANIZATION APP
# class OrganizationCreateUpdateSuccessUrlMixin(ModelFormMixin):
#   def get_success_url(self):
#     return reverse('organization_settings')
  
# class OrganizationDeleteSuccessUrlMixin(DeletionMixin):
#   def get_success_url(self):
#     return reverse('organization_settings')

# class ProjectPhaseObjectMixin(SingleObjectMixin):
#   model = ProjectPhase

# class DisciplineObjectMixin(SingleObjectMixin):
#   model = Discipline

# class AuthoringSoftwareObjectMixin(SingleObjectMixin):
#   model = AuthoringSoftware

# class LodReferenceObjectMixin(SingleObjectMixin):
#   model = LodReference

# class BimSpecificationObjectMixin(SingleObjectMixin):
#   model = BimSpecification

# class BimExpertObjectMixin(SingleObjectMixin):
#   model = BimExpert

