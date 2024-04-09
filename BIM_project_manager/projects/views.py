from typing import Any
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import BimProject, BimModel, InfoSheet, Report, ClashTest, ValidationTest
from .mixins import StaffMixin
from .utils import create_model_register_file, create_project_info_sheets_file, create_model_info_sheets_file, set_default_coordination, set_default_validation

# Create your views here.

class CreateBimProject(StaffMixin, CreateView):
  model = BimProject
  fields = ['name', 'description', 'customer', 'address', 'phase']
  template_name = 'projects/create_bim_project.html'
  success_url = '/'

class UpdateBimProject(StaffMixin, UpdateView):
  model = BimProject
  fields = ['name', 'description', 'customer', 'address', 'phase']
  template_name_suffix = "_update_form"

  def get_success_url(self):
    return reverse('manage_project', kwargs={'pk': self.object.pk})

class DeleteBimProject(StaffMixin, DeleteView):
  model = BimProject
  success_url = '/'

class ManageBimProject(StaffMixin, DetailView):
  model = BimProject
  template_name = 'projects/manage_bim_project.html'


class CreateBimModel(StaffMixin, CreateView):
  model = BimModel
  fields = ['name', 'discipline', 'designer', 'authoringSoftware', 'lodReference']
  template_name = 'projects/create_bim_model.html'

  def form_valid(self, form):
    bim_project = get_object_or_404(BimProject, pk=self.kwargs['pk'])
    form.instance.project = bim_project
    return super(CreateBimModel, self).form_valid(form)
  
  def get_success_url(self):
    return reverse('manage_project', kwargs={ 'pk': self.object.project.pk })

class UpdateBimModel(StaffMixin, UpdateView):
  model = BimModel
  fields = ['name', 'discipline', 'designer', 'authoringSoftware', 'lodReference']
  template_name_suffix = "_update_form"

  def get_success_url(self):
    return reverse('manage_bim_model', kwargs={'pk': self.object.pk})

class DeleteBimModel(StaffMixin, DeleteView):
  model = BimModel

  def get_success_url(self):
    return reverse('manage_project', kwargs={'pk': self.object.project.pk})

class ManageBimModel(StaffMixin, DetailView):
  model = BimModel
  template_name = 'projects/manage_bim_model.html'

  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context['info_sheets_coordination'] = self.object.info_sheets.filter(sheet_type='coordination')
    context['info_sheets_validation'] = self.object.info_sheets.filter(sheet_type='validation')
    return context


class CreateInfoSheet(StaffMixin, CreateView):
  model = InfoSheet
  fields = ['name', 'description']
  template_name = 'projects/create_info_sheet.html'

  def form_valid(self, form):
    bim_model = get_object_or_404(BimModel, pk=self.kwargs['pk'])
    form.instance.bim_model = bim_model
    form.instance.sheet_type = self.kwargs['sheet_type']
    return super(CreateInfoSheet, self).form_valid(form)
  
  def get_success_url(self):
    return reverse('manage_bim_model', kwargs={ 'pk': self.object.bim_model.pk })

class UpdateInfoSheet(StaffMixin, UpdateView):
  model = InfoSheet
  fields = ['name', 'description', 'sheet_type']
  template_name_suffix = "_update_form"

  def get_success_url(self):
    return reverse('manage_info_sheet', kwargs={'pk': self.object.pk})

class DeleteInfoSheet(StaffMixin, DeleteView):
  model = InfoSheet

  def get_success_url(self):
    return reverse('manage_bim_model', kwargs={'pk': self.object.bim_model.pk})

class ManageInfoSheet(StaffMixin, DetailView):
  model = InfoSheet
  template_name = 'projects/manage_info_sheet.html'


class CreateReport(StaffMixin, CreateView):
  model = Report
  fields = ['name', 'description']
  template_name = 'projects/create_report.html'

  def form_valid(self, form):
    info_sheet = get_object_or_404(InfoSheet, pk=self.kwargs['pk'])
    form.instance.info_sheet = info_sheet
    return super(CreateReport, self).form_valid(form)
  
  def get_success_url(self):
    return reverse('manage_info_sheet', kwargs={ 'pk': self.object.info_sheet.pk })

class UpdateReport(StaffMixin, UpdateView):
  model = Report
  fields = ['name', 'description']
  template_name_suffix = "_update_form"

  def get_success_url(self):
    return reverse('manage_report', kwargs={'pk': self.object.pk})

class DeleteReport(StaffMixin, DeleteView):
  model = Report

  def get_success_url(self):
    return reverse('manage_info_sheet', kwargs={'pk': self.object.info_sheet.pk})

@login_required
def manage_report_view(request, pk):
  report = get_object_or_404(Report, pk=pk)
  tests = None
  if report.info_sheet.sheet_type == 'coordination':
    tests = ClashTest.objects.filter(report=report).order_by('date')
  elif report.info_sheet.sheet_type == 'validation':
    tests = ValidationTest.objects.filter(report=report).order_by('date')
  context = {'report': report, 'tests': tests}
  return render(request, 'projects/manage_report.html', context)


class CreateClashTest(StaffMixin, CreateView):
  model = ClashTest
  fields = ['comments', 'clash_new', 'clash_active', 'clash_reviewed', 'clash_approved', 'clash_resolved']
  template_name = 'projects/create_clash_test.html'

  def form_valid(self, form):
    report = get_object_or_404(Report, pk=self.kwargs['pk'])
    form.instance.report = report
    return super(CreateClashTest, self).form_valid(form)
  
  def get_success_url(self):
    return reverse('manage_report', kwargs={ 'pk': self.object.report.pk })

class UpdateClashTest(StaffMixin, UpdateView):
  model = ClashTest
  fields = ['comments', 'clash_new', 'clash_active', 'clash_reviewed', 'clash_approved', 'clash_resolved']
  template_name_suffix = "_update_form"

  def get_success_url(self):
    return reverse('manage_report', kwargs={'pk': self.object.report.pk})

class DeleteClashTest(StaffMixin, DeleteView):
  model = ClashTest

  def get_success_url(self):
    return reverse('manage_report', kwargs={'pk': self.object.report.pk})


class CreateValidationTest(StaffMixin, CreateView):
  model = ValidationTest
  fields = ['comments', 'specification', 'issues']
  template_name = 'projects/create_validation_test.html'

  def form_valid(self, form):
    report = get_object_or_404(Report, pk=self.kwargs['pk'])
    form.instance.report = report
    return super(CreateValidationTest, self).form_valid(form)
  
  def get_success_url(self):
    return reverse('manage_report', kwargs={ 'pk': self.object.report.pk })

class UpdateValidationTest(StaffMixin, UpdateView):
  model = ValidationTest
  fields = ['comments', 'specification', 'issues']
  template_name_suffix = "_update_form"

  def get_success_url(self):
    return reverse('manage_report', kwargs={'pk': self.object.report.pk})

class DeleteValidationTest(StaffMixin, DeleteView):
  model = ValidationTest

  def get_success_url(self):
    return reverse('manage_report', kwargs={'pk': self.object.report.pk})


@login_required  
def default_coordination(request, pk):
  bim_model = get_object_or_404(BimModel, pk=pk)

  if bim_model.default_coordination:
    return HttpResponseRedirect(bim_model.get_absolute_url())

  set_default_coordination(bim_model)

  bim_model.default_coordination = True
  bim_model.save()

  return HttpResponseRedirect(bim_model.get_absolute_url())

@login_required
def default_validation(request, pk):
  bim_model = get_object_or_404(BimModel, pk=pk)

  if bim_model.default_validation:
    return HttpResponseRedirect(bim_model.get_absolute_url())
  
  set_default_validation(bim_model)

  bim_model.default_validation = True
  bim_model.save()

  return HttpResponseRedirect(bim_model.get_absolute_url())

@login_required
def export_model_register(request, pk):
  project = get_object_or_404(BimProject, pk=pk)
  return create_model_register_file(project)

@login_required
def export_project_info_sheets(request, pk):
  project = get_object_or_404(BimProject, pk=pk)
  return create_project_info_sheets_file(project)

@login_required
def export_model_info_sheets(request, pk):
  bim_model = get_object_or_404(BimModel, pk=pk)
  return create_model_info_sheets_file(bim_model)