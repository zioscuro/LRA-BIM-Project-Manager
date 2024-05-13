from django.shortcuts import render
from core.mixins import StaffMixin
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


class CreateProjectPhase(StaffMixin, CreateView):
  model = ProjectPhase
  fields = ['name', 'description']
  template_name = 'organization/project_phase_create.html'
  
  def get_success_url(self):
    return reverse('organization_settings')

class UpdateProjectPhase(StaffMixin, UpdateView):
  model = ProjectPhase
  fields = ['name', 'description']
  template_name = 'organization/project_phase_update.html'

  def get_success_url(self):
    return reverse('organization_settings')

class DeleteProjectPhase(StaffMixin, DeleteView):
  model = ProjectPhase
  template_name = 'organization/project_phase_delete.html'

  def get_success_url(self):
    return reverse('organization_settings')


class CreateDiscipline(StaffMixin, CreateView):
  model = Discipline
  fields = ['name', 'description']
  template_name = 'organization/discipline_create.html'
  
  def get_success_url(self):
    return reverse('organization_settings')

class UpdateDiscipline(StaffMixin, UpdateView):
  model = Discipline
  fields = ['name', 'description', 'code']
  template_name = 'organization/discipline_update.html'

  def get_success_url(self):
    return reverse('organization_settings')

class DeleteDiscipline(StaffMixin, DeleteView):
  model = Discipline
  template_name = 'organization/discipline_delete.html'

  def get_success_url(self):
    return reverse('organization_settings')


class CreateAuthoringSoftware(StaffMixin, CreateView):
  model = AuthoringSoftware
  fields = ['name', 'version']
  template_name = 'organization/authoring_software_create.html'
  
  def get_success_url(self):
    return reverse('organization_settings')

class UpdateAuthoringSoftware(StaffMixin, UpdateView):
  model = AuthoringSoftware
  fields = ['name', 'version']
  template_name = 'organization/authoring_software_update.html'

  def get_success_url(self):
    return reverse('organization_settings')

class DeleteAuthoringSoftware(StaffMixin, DeleteView):
  model = AuthoringSoftware
  template_name = 'organization/authoring_software_delete.html'

  def get_success_url(self):
    return reverse('organization_settings')


class CreateLodReference(StaffMixin, CreateView):
  model = LodReference
  fields = ['name', 'description']
  template_name = 'organization/lod_reference_create.html'
  
  def get_success_url(self):
    return reverse('organization_settings')

class UpdateLodReference(StaffMixin, UpdateView):
  model = LodReference
  fields = ['name', 'description']
  template_name = 'organization/lod_reference_update.html'

  def get_success_url(self):
    return reverse('organization_settings')

class DeleteLodReference(StaffMixin, DeleteView):
  model = LodReference
  template_name = 'organization/lod_reference_delete.html'

  def get_success_url(self):
    return reverse('organization_settings')


class CreateBimSpecification(StaffMixin, CreateView):
  model = BimSpecification
  fields = ['name', 'description']
  template_name = 'organization/specification_create.html'
  
  def get_success_url(self):
    return reverse('organization_settings')

class UpdateBimSpecification(StaffMixin, UpdateView):
  model = BimSpecification
  fields = ['name', 'description']
  template_name = 'organization/specification_update.html'

  def get_success_url(self):
    return reverse('organization_settings')

class DeleteBimSpecification(StaffMixin, DeleteView):
  model = BimSpecification
  template_name = 'organization/specification_delete.html'

  def get_success_url(self):
    return reverse('organization_settings')


class CreateBimExpert(StaffMixin, CreateView):
  model = BimExpert
  fields = ['name', 'position']
  template_name = 'organization/bim_expert_create.html'
  
  def get_success_url(self):
    return reverse('organization_settings')

class UpdateBimExpert(StaffMixin, UpdateView):
  model = BimExpert
  fields = ['name', 'position']
  template_name = 'organization/bim_expert_update.html'

  def get_success_url(self):
    return reverse('organization_settings')

class DeleteBimExpert(StaffMixin, DeleteView):
  model = BimExpert
  template_name = 'organization/bim_expert_delete.html'

  def get_success_url(self):
    return reverse('organization_settings')