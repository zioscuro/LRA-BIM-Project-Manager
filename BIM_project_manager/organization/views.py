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
  pass

class UpdateDiscipline(StaffMixin, UpdateView):
  pass

class DeleteDiscipline(StaffMixin, DeleteView):
  pass


class CreateAuthoringSoftware(StaffMixin, CreateView):
  pass

class UpdateAuthoringSoftware(StaffMixin, UpdateView):
  pass

class DeleteAuthoringSoftware(StaffMixin, DeleteView):
  pass


class CreateLodReference(StaffMixin, CreateView):
  pass

class UpdateLodReference(StaffMixin, UpdateView):
  pass

class DeleteLodReference(StaffMixin, DeleteView):
  pass


class CreateBimSpecification(StaffMixin, CreateView):
  pass

class UpdateBimSpecification(StaffMixin, UpdateView):
  pass

class DeleteBimSpecification(StaffMixin, DeleteView):
  pass


class CreateBimExpert(StaffMixin, CreateView):
  pass

class UpdateBimExpert(StaffMixin, UpdateView):
  pass

class DeleteBimExpert(StaffMixin, DeleteView):
  pass