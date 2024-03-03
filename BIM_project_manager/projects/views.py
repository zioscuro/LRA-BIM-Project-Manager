from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, DeleteView
from django.http import HttpResponseRedirect

from .forms import AddBimModelForm, AddInfoSheetForm, AddReportForm, AddClashTestForm, AddValidationTestForm
from .models import BimProject, BimModel, InfoSheet, Report, ClashTest, ValidationTest
from .mixins import StaffMixin

# Create your views here.

class CreateBimProject(StaffMixin, CreateView):
  model = BimProject
  fields = '__all__'
  template_name = 'projects/create_project.html'
  success_url = '/'

class DeleteBimProject(StaffMixin, DeleteView):
  model = BimProject
  success_url = '/'

@login_required
def manage_project_view(request, pk):
  project = get_object_or_404(BimProject, pk=pk)
  bim_models = BimModel.objects.filter(project=project).order_by('name')
  context = {'project': project, 'bim_models': bim_models}
  return render(request, 'projects/manage_project.html', context)

@login_required
def add_bim_model_view(request, pk):
  project = get_object_or_404(BimProject, pk=pk)
  if request.method == 'POST':
    form = AddBimModelForm(request.POST)
    if form.is_valid():
      bim_model = form.save(commit=False)
      bim_model.project = project
      bim_model.save()
      return HttpResponseRedirect(project.get_absolute_url())
  else:
    form = AddBimModelForm()
  context = {'form': form, 'project': project}
  return render(request, 'projects/add_bim_model.html', context)

@login_required
def manage_bim_model_view(request, pk):
  bim_model = get_object_or_404(BimModel, pk=pk)
  info_sheets_coordination = InfoSheet.objects.filter(bim_model=bim_model, sheet_type='coordination')
  info_sheets_validation = InfoSheet.objects.filter(bim_model=bim_model, sheet_type='validation')
  context = {'bim_model': bim_model, 'info_sheets_coordination': info_sheets_coordination, 'info_sheets_validation': info_sheets_validation}
  return render(request, 'projects/manage_model.html', context)

class DeleteBimModel(StaffMixin, DeleteView):
  model = BimModel
  success_url = '/'

@login_required
def add_info_sheet_view(request, pk, sheet_type):
  bim_model = get_object_or_404(BimModel, pk=pk)
  if request.method == 'POST':
    form = AddInfoSheetForm(request.POST)
    if form.is_valid():
      info_sheet = form.save(commit=False)
      info_sheet.sheet_type = sheet_type
      info_sheet.bim_model = bim_model
      info_sheet.save()
      return HttpResponseRedirect(bim_model.get_absolute_url())
  else:
    form = AddInfoSheetForm()
  context = {'form': form, 'bim_model': bim_model, 'sheet_type': sheet_type}
  return render(request, 'projects/add_info_sheet.html', context)

@login_required
def manage_info_sheet_view(request, pk):
  info_sheet = get_object_or_404(InfoSheet, pk=pk)
  reports = Report.objects.filter(info_sheet=info_sheet)
  context = {'info_sheet': info_sheet, 'reports': reports}
  return render(request, 'projects/manage_info_sheet.html', context)

class DeleteInfoSheet(StaffMixin, DeleteView):
  model = InfoSheet
  success_url = '/'

@login_required
def add_report_view(request, pk):
  info_sheet = get_object_or_404(InfoSheet, pk=pk)
  if request.method == 'POST':
    form = AddReportForm(request.POST)
    if form.is_valid():
      report = form.save(commit=False)
      report.info_sheet = info_sheet
      report.save()
      return HttpResponseRedirect(info_sheet.get_absolute_url())
  else:
    form = AddInfoSheetForm()
  context = {'form': form, 'info_sheet': info_sheet}
  return render(request, 'projects/add_report.html', context)

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

class DeleteReport(StaffMixin, DeleteView):
  model = Report
  success_url = '/'

@login_required
def add_clash_test_view(request, pk):
  report = get_object_or_404(Report, pk=pk)
  if request.method == 'POST':
    form = AddClashTestForm(request.POST)
    if form.is_valid():
      test = form.save(commit=False)
      test.report = report
      test.save()
      return HttpResponseRedirect(report.get_absolute_url())
  else:
    form = AddClashTestForm()
  context = {'form': form, 'report': report}
  return render(request, 'projects/add_clash_test.html', context)

class DeleteClashTest(StaffMixin, DeleteView):
  model = ClashTest
  success_url = '/'

@login_required
def add_validation_test_view(request, pk):
  report = get_object_or_404(Report, pk=pk)
  if request.method == 'POST':
    form = AddValidationTestForm(request.POST)
    if form.is_valid():
      test = form.save(commit=False)
      test.report = report
      test.save()
      return HttpResponseRedirect(report.get_absolute_url())
  else:
    form = AddValidationTestForm()
  context = {'form': form, 'report': report}
  return render(request, 'projects/add_validation_test.html', context)

class DeleteValidationTest(StaffMixin, DeleteView):
  model = ValidationTest
  success_url = '/'