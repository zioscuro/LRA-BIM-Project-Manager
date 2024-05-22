from django.shortcuts import render
from core.mixins import StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, OrganizationDeleteSuccessUrlMixin, ProjectPhaseObjectMixin, DisciplineObjectMixin, AuthoringSoftwareObjectMixin, LodReferenceObjectMixin, BimSpecificationObjectMixin, BimExpertObjectMixin
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
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


class CreateProjectPhase(StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, ProjectPhaseObjectMixin, CreateView):
  fields = '__all__'
  template_name = 'organization/project_phase_create.html'  

class UpdateProjectPhase(StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, ProjectPhaseObjectMixin, UpdateView):
  fields = '__all__'
  template_name = 'organization/project_phase_update.html'

class DeleteProjectPhase(StaffMixin, OrganizationDeleteSuccessUrlMixin, ProjectPhaseObjectMixin, DeleteView):
  template_name = 'organization/project_phase_delete.html'


class CreateDiscipline(StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, DisciplineObjectMixin, CreateView):
  fields = '__all__'
  template_name = 'organization/discipline_create.html'
  
class UpdateDiscipline(StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, DisciplineObjectMixin, UpdateView):
  fields = '__all__'
  template_name = 'organization/discipline_update.html'

class DeleteDiscipline(StaffMixin, OrganizationDeleteSuccessUrlMixin, DisciplineObjectMixin, DeleteView):
  template_name = 'organization/discipline_delete.html'


class CreateAuthoringSoftware(StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, AuthoringSoftwareObjectMixin, CreateView):
  fields = '__all__'
  template_name = 'organization/authoring_software_create.html'
  
class UpdateAuthoringSoftware(StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, AuthoringSoftwareObjectMixin, UpdateView):
  fields = '__all__'
  template_name = 'organization/authoring_software_update.html'

class DeleteAuthoringSoftware(StaffMixin, OrganizationDeleteSuccessUrlMixin, AuthoringSoftwareObjectMixin, DeleteView):
  template_name = 'organization/authoring_software_delete.html'


class CreateLodReference(StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, LodReferenceObjectMixin, CreateView):
  fields = '__all__'
  template_name = 'organization/lod_reference_create.html'
  
class UpdateLodReference(StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, LodReferenceObjectMixin, UpdateView):
  model = LodReference
  fields = '__all__'
  template_name = 'organization/lod_reference_update.html'

class DeleteLodReference(StaffMixin, OrganizationDeleteSuccessUrlMixin, LodReferenceObjectMixin, DeleteView):
  model = LodReference
  template_name = 'organization/lod_reference_delete.html'


class CreateBimSpecification(StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, BimSpecificationObjectMixin, CreateView):
  model = BimSpecification
  fields = '__all__'
  template_name = 'organization/specification_create.html'
  
class UpdateBimSpecification(StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, BimSpecificationObjectMixin, UpdateView):
  fields = '__all__'
  template_name = 'organization/specification_update.html'

class DeleteBimSpecification(StaffMixin, OrganizationDeleteSuccessUrlMixin, BimSpecificationObjectMixin, DeleteView):
  template_name = 'organization/specification_delete.html'


class CreateBimExpert(StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, BimExpertObjectMixin, CreateView):
  fields = '__all__'
  template_name = 'organization/bim_expert_create.html'

class UpdateBimExpert(StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, BimExpertObjectMixin, UpdateView):
  fields = '__all__'
  template_name = 'organization/bim_expert_update.html'

class DeleteBimExpert(StaffMixin, OrganizationDeleteSuccessUrlMixin, BimExpertObjectMixin, DeleteView):
  template_name = 'organization/bim_expert_delete.html'
