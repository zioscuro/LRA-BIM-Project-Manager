from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect

from .forms import AddBimModelForm, AddInfoSheetForm
from .models import BimProject, BimModel, InfoSheet
from .mixins import StaffMixin

# Create your views here.

class CreateBimProject(StaffMixin, CreateView):
  model = BimProject
  fields = '__all__'
  template_name = 'projects/create_project.html'
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
