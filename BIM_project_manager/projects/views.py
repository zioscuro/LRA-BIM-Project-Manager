from typing import Any
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse

from .models import BimProject, BimModel, InfoSheet, Report, ClashTest, ValidationTest
from .forms import BimModelCreateForm, BimModelUpdateForm, ReportForm, ClashTestForm, ValidationTestForm, UploadFileForm, MultipleUploadFileForm
from core.mixins import StaffMixin
from .utils import ExcelExporter, set_default_coordination, set_default_validation, handle_model_register_import, handle_coordination_reports_import, handle_validation_reports_import, handle_report_list_import

# Create your views here.

class CreateBimProject(StaffMixin, CreateView):
  model = BimProject
  fields = '__all__'
  template_name = 'projects/bim_project_create.html'
  success_url = '/'

class UpdateBimProject(StaffMixin, UpdateView):
  model = BimProject
  fields = '__all__'
  template_name = 'projects/bim_project_update.html'

  def get_success_url(self):
    return reverse('manage_project', kwargs={'pk': self.object.pk})

class DeleteBimProject(StaffMixin, DeleteView):
  model = BimProject
  template_name = 'projects/bim_project_delete.html'
  success_url = '/'

class ManageBimProject(StaffMixin, DetailView):
  model = BimProject
  template_name = 'projects/manage_bim_project.html'


class CreateBimModel(StaffMixin, CreateView):
  model = BimModel
  form_class = BimModelCreateForm
  template_name = 'projects/bim_model_create.html'

  def form_valid(self, form):
    bim_project = get_object_or_404(BimProject, pk=self.kwargs['pk'])
    form.instance.bim_project = bim_project
    form.instance.designer = bim_project.default_designer
    form.instance.bim_manager = bim_project.default_bim_manager
    form.instance.bim_coordinator = bim_project.default_bim_coordinator
    form.instance.bim_specialist = bim_project.default_bim_specialist
    return super(CreateBimModel, self).form_valid(form)
  
  def get_success_url(self):
    return reverse('manage_project', kwargs={ 'pk': self.object.bim_project.pk })

class UpdateBimModel(StaffMixin, UpdateView):
  model = BimModel
  form_class = BimModelUpdateForm
  template_name = 'projects/bim_model_update.html'

  def get_success_url(self):
    return reverse('manage_bim_model', kwargs={'pk': self.object.pk})

class DeleteBimModel(StaffMixin, DeleteView):
  model = BimModel
  template_name = 'projects/bim_model_delete.html'

  def get_success_url(self):
    return reverse('manage_project', kwargs={'pk': self.object.bim_project.pk})

class ManageBimModel(StaffMixin, DetailView):
  model = BimModel
  template_name = 'projects/manage_bim_model.html'

  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context['info_sheets_coordination'] = self.object.info_sheets.filter(sheet_type='Coordination')
    context['info_sheets_validation'] = self.object.info_sheets.filter(sheet_type='Validation')
    return context


class CreateInfoSheet(StaffMixin, CreateView):
  model = InfoSheet
  fields = ['name', 'description']
  template_name = 'projects/info_sheet_create.html'

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
  template_name = 'projects/info_sheet_update.html'

  def get_success_url(self):
    return reverse('manage_info_sheet', kwargs={'pk': self.object.pk})

class DeleteInfoSheet(StaffMixin, DeleteView):
  model = InfoSheet
  template_name = 'projects/info_sheet_delete.html'

  def get_success_url(self):
    return reverse('manage_bim_model', kwargs={'pk': self.object.bim_model.pk})

class ManageInfoSheet(StaffMixin, DetailView):
  model = InfoSheet
  template_name = 'projects/manage_info_sheet.html'


class CreateReport(StaffMixin, CreateView):
  model = Report
  form_class = ReportForm
  template_name = 'projects/report_create.html'

  def form_valid(self, form):
    info_sheet = get_object_or_404(InfoSheet, pk=self.kwargs['pk'])
    form.instance.info_sheet = info_sheet
    return super(CreateReport, self).form_valid(form)
  
  def get_success_url(self):
    return reverse('manage_info_sheet', kwargs={ 'pk': self.object.info_sheet.pk })

class UpdateReport(StaffMixin, UpdateView):
  model = Report
  form_class = ReportForm
  template_name = 'projects/report_update.html'

  def get_success_url(self):
    return reverse('manage_report', kwargs={'pk': self.object.pk})

class DeleteReport(StaffMixin, DeleteView):
  model = Report
  template_name = 'projects/report_delete.html'

  def get_success_url(self):
    return reverse('manage_info_sheet', kwargs={'pk': self.object.info_sheet.pk})

class ManageReport(StaffMixin, DetailView):
  model = Report
  template_name = 'projects/manage_report.html'


class CreateClashTest(StaffMixin, CreateView):
  model = ClashTest
  form_class = ClashTestForm
  template_name = 'projects/clash_test_create.html'

  def form_valid(self, form):
    report = get_object_or_404(Report, pk=self.kwargs['pk'])
    form.instance.report = report
    return super(CreateClashTest, self).form_valid(form)
  
  def get_success_url(self):
    return reverse('manage_report', kwargs={ 'pk': self.object.report.pk })

class UpdateClashTest(StaffMixin, UpdateView):
  model = ClashTest
  form_class = ClashTestForm
  template_name = 'projects/clash_test_update.html'

  def get_success_url(self):
    return reverse('manage_report', kwargs={'pk': self.object.report.pk})

class DeleteClashTest(StaffMixin, DeleteView):
  model = ClashTest
  template_name = 'projects/clash_test_delete.html'

  def get_success_url(self):
    return reverse('manage_report', kwargs={'pk': self.object.report.pk})


class CreateValidationTest(StaffMixin, CreateView):
  model = ValidationTest
  form_class = ValidationTestForm
  template_name = 'projects/validation_test_create.html'

  def form_valid(self, form):
    report = get_object_or_404(Report, pk=self.kwargs['pk'])
    form.instance.report = report
    return super(CreateValidationTest, self).form_valid(form)
  
  def get_success_url(self):
    return reverse('manage_report', kwargs={ 'pk': self.object.report.pk })

class UpdateValidationTest(StaffMixin, UpdateView):
  model = ValidationTest
  form_class = ValidationTestForm
  template_name = 'projects/validation_test_update.html'

  def get_success_url(self):
    return reverse('manage_report', kwargs={'pk': self.object.report.pk})

class DeleteValidationTest(StaffMixin, DeleteView):
  model = ValidationTest
  template_name = 'projects/validation_test_delete.html'

  def get_success_url(self):
    return reverse('manage_report', kwargs={'pk': self.object.report.pk})


class DefaultInfoSheet(StaffMixin, View):  
  def get(self, request, pk, sheet_type):
    bim_model = get_object_or_404(BimModel, pk=pk)

    if sheet_type == 'Coordination':
      if bim_model.default_coordination:
        return HttpResponseRedirect(bim_model.get_absolute_url())
      set_default_coordination(bim_model)
      bim_model.default_coordination = True

    if sheet_type == 'Validation':
      if bim_model.default_validation:
        return HttpResponseRedirect(bim_model.get_absolute_url())
      set_default_validation(bim_model)
      bim_model.default_validation = True

    bim_model.save()
    return HttpResponseRedirect(bim_model.get_absolute_url())

class BimDataExporter(StaffMixin, View):
  def get(self, request, pk, export_type):
    if export_type == 'model_register':
      project = get_object_or_404(BimProject, pk=pk)
      exporter = ExcelExporter(project)
      return exporter.export_model_register()

    if export_type == 'project_info_sheets':
      project = get_object_or_404(BimProject, pk=pk)
      exporter = ExcelExporter(project)
      return exporter.export_project_info_sheets()
    
    if export_type == 'model_info_sheets':
      bim_model = get_object_or_404(BimModel, pk=pk)
      exporter = ExcelExporter(bim_model)
      return exporter.export_model_info_sheets()    

    return HttpResponseBadRequest("Bad request.")

class BimDataImporter(StaffMixin, View):
  def post(self, request, pk, import_type):
    form = UploadFileForm(request.POST, request.FILES)
    bim_project = get_object_or_404(BimProject, pk=pk)
    
    if import_type == 'model_register':
      if form.is_valid():
        handle_model_register_import(request.FILES["file"], bim_project)
        return HttpResponseRedirect(bim_project.get_absolute_url())
      
    if import_type == 'report_list':
      if form.is_valid():
        handle_report_list_import(request.FILES["file"], bim_project)
        return HttpResponseRedirect(bim_project.get_absolute_url())
    
    if import_type == 'coordination_reports':
      if form.is_valid():
        handle_coordination_reports_import(request.FILES["file"], bim_project)
        return HttpResponseRedirect(bim_project.get_absolute_url())

    if import_type == 'validation_reports':
      form = MultipleUploadFileForm(request.POST, request.FILES)
      if form.is_valid():
        files = form.cleaned_data['file_field']
        for f in files:
          print(f)         
          handle_validation_reports_import(f, bim_project)
          
        return HttpResponseRedirect(bim_project.get_absolute_url())
    
    return HttpResponseBadRequest("Bad request.")
  
  def get(self, request, pk, import_type):
    form = UploadFileForm()
    if import_type == 'model_register':
      return render(request, 'projects/upload_model_register.html', {"form": form})
    
    if import_type == 'report_list':
      return render(request, 'projects/upload_report_list.html', {"form": form})    
    
    if import_type == 'coordination_reports':
      return render(request, 'projects/upload_coordination_reports.html', {"form": form})

    if import_type == 'validation_reports':
      form = MultipleUploadFileForm()
      return render(request, 'projects/upload_validation_reports.html', {"form": form})
 
    return HttpResponseBadRequest("Bad request.")

# class ValidationDataForm(FormView):
#   form_class = MultipleFileFieldForm
#   template_name = 'projects/upload_validation_reports.html'
#   success_url = '/'
  
#   def form_valid(self, form):
#     files = form.cleaned_data['file_field']
#     for f in files:
#       print(f)            
#     return super().form_valid(form)
  
#   def post(self, request, pk):   
#     super()
  
#   def get(self, request, pk):
#     super()

   
