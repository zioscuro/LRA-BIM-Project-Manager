from django.shortcuts import render
from core.mixins import StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, OrganizationDeleteSuccessUrlMixin
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from organization.models import ProjectPhase, Discipline, AuthoringSoftware, LodReference, BimSpecification, BimExpert
from django.urls import reverse


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


class CreateProjectPhase(StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, CreateView):
  model = ProjectPhase
  fields = '__all__'
  template_name = 'organization/project_phase_create.html'
  
  # def get_success_url(self):
  #   return reverse('organization_settings')

class UpdateProjectPhase(StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, UpdateView):
  model = ProjectPhase
  fields = '__all__'
  template_name = 'organization/project_phase_update.html'

  # def get_success_url(self):
  #   return reverse('organization_settings')

class DeleteProjectPhase(StaffMixin, OrganizationDeleteSuccessUrlMixin, DeleteView):
  model = ProjectPhase
  template_name = 'organization/project_phase_delete.html'


class CreateDiscipline(StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, CreateView):
  model = Discipline
  fields = '__all__'
  template_name = 'organization/discipline_create.html'
  
class UpdateDiscipline(StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, UpdateView):
  model = Discipline
  fields = '__all__'
  template_name = 'organization/discipline_update.html'

class DeleteDiscipline(StaffMixin, OrganizationDeleteSuccessUrlMixin, DeleteView):
  model = Discipline
  template_name = 'organization/discipline_delete.html'


class CreateAuthoringSoftware(StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, CreateView):
  model = AuthoringSoftware
  fields = '__all__'
  template_name = 'organization/authoring_software_create.html'
  
class UpdateAuthoringSoftware(StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, UpdateView):
  model = AuthoringSoftware
  fields = '__all__'
  template_name = 'organization/authoring_software_update.html'

class DeleteAuthoringSoftware(StaffMixin, OrganizationDeleteSuccessUrlMixin, DeleteView):
  model = AuthoringSoftware
  template_name = 'organization/authoring_software_delete.html'


class CreateLodReference(StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, CreateView):
  model = LodReference
  fields = '__all__'
  template_name = 'organization/lod_reference_create.html'
  
class UpdateLodReference(StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, UpdateView):
  model = LodReference
  fields = '__all__'
  template_name = 'organization/lod_reference_update.html'

class DeleteLodReference(StaffMixin, OrganizationDeleteSuccessUrlMixin, DeleteView):
  model = LodReference
  template_name = 'organization/lod_reference_delete.html'


class CreateBimSpecification(StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, CreateView):
  model = BimSpecification
  fields = '__all__'
  template_name = 'organization/specification_create.html'
  
class UpdateBimSpecification(StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, UpdateView):
  model = BimSpecification
  fields = '__all__'
  template_name = 'organization/specification_update.html'

class DeleteBimSpecification(StaffMixin, OrganizationDeleteSuccessUrlMixin, DeleteView):
  model = BimSpecification
  template_name = 'organization/specification_delete.html'


class CreateBimExpert(StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, CreateView):
  model = BimExpert
  fields = '__all__'
  template_name = 'organization/bim_expert_create.html'

class UpdateBimExpert(StaffMixin, OrganizationCreateUpdateSuccessUrlMixin, UpdateView):
  model = BimExpert
  fields = '__all__'
  template_name = 'organization/bim_expert_update.html'

class DeleteBimExpert(StaffMixin, OrganizationDeleteSuccessUrlMixin, DeleteView):
  model = BimExpert
  template_name = 'organization/bim_expert_delete.html'
