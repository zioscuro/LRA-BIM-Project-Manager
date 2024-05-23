from django.shortcuts import render
from core.mixins import StaffMixin
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from organization.mixins import OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView, ProjectPhaseViewMixin, DisciplineViewMixin, AuthoringSoftwareViewMixin, LodReferenceViewMixin, BimSpecificationViewMixin, BimExpertViewMixin
from organization.models import ProjectPhase, Discipline, AuthoringSoftware, LodReference, BimSpecification, BimExpert

# Create your views here.

class OrganizationSettings(StaffMixin, View):
  def get(self, request):
    project_phases = ProjectPhase.objects.all()
    disciplines = Discipline.objects.all()
    software_list = AuthoringSoftware.objects.all()
    lod_list = LodReference.objects.all()
    specifications_list = BimSpecification.objects.all()
    expert_list = BimExpert.objects.all()

    context = {
      'project_phases': project_phases,
      'disciplines': disciplines,
      'software_list': software_list,
      'lod_list': lod_list,
      'specifications_list': specifications_list, 
      'expert_list': expert_list 
      }

    return render(request, 'organization/organization_settings.html', context)


class CreateProjectPhase(ProjectPhaseViewMixin, OrganizationCreateView):
  fields = '__all__'
  template_name = 'organization/project_phase_create.html'  

class UpdateProjectPhase(ProjectPhaseViewMixin, OrganizationUpdateView):
  fields = '__all__'
  template_name = 'organization/project_phase_update.html'

class DeleteProjectPhase(ProjectPhaseViewMixin, OrganizationDeleteView):
  template_name = 'organization/project_phase_delete.html'


class CreateDiscipline(DisciplineViewMixin, OrganizationCreateView):
  fields = '__all__'
  template_name = 'organization/discipline_create.html'
  
class UpdateDiscipline(DisciplineViewMixin, OrganizationUpdateView):
  fields = '__all__'
  template_name = 'organization/discipline_update.html'

class DeleteDiscipline(DisciplineViewMixin, OrganizationDeleteView):
  template_name = 'organization/discipline_delete.html'


class CreateAuthoringSoftware(AuthoringSoftwareViewMixin, OrganizationCreateView):
  fields = '__all__'
  template_name = 'organization/authoring_software_create.html'
  
class UpdateAuthoringSoftware(AuthoringSoftwareViewMixin, OrganizationUpdateView):
  fields = '__all__'
  template_name = 'organization/authoring_software_update.html'

class DeleteAuthoringSoftware(AuthoringSoftwareViewMixin, OrganizationDeleteView):
  template_name = 'organization/authoring_software_delete.html'


class CreateLodReference(LodReferenceViewMixin, OrganizationCreateView):
  fields = '__all__'
  template_name = 'organization/lod_reference_create.html'
  
class UpdateLodReference(LodReferenceViewMixin, OrganizationUpdateView):
  fields = '__all__'
  template_name = 'organization/lod_reference_update.html'

class DeleteLodReference(LodReferenceViewMixin, OrganizationDeleteView):
  template_name = 'organization/lod_reference_delete.html'


class CreateBimSpecification(BimSpecificationViewMixin, OrganizationCreateView):
  fields = '__all__'
  template_name = 'organization/specification_create.html'
  
class UpdateBimSpecification(BimSpecificationViewMixin, OrganizationUpdateView):
  fields = '__all__'
  template_name = 'organization/specification_update.html'

class DeleteBimSpecification(BimSpecificationViewMixin, OrganizationDeleteView):
  template_name = 'organization/specification_delete.html'


class CreateBimExpert(BimExpertViewMixin, OrganizationCreateView):
  fields = '__all__'
  template_name = 'organization/bim_expert_create.html'

class UpdateBimExpert(BimExpertViewMixin, OrganizationUpdateView):
  fields = '__all__'
  template_name = 'organization/bim_expert_update.html'

class DeleteBimExpert(BimExpertViewMixin, OrganizationDeleteView):
  template_name = 'organization/bim_expert_delete.html'
