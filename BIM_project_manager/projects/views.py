from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect

from .forms import AddBimModelForm
from .models import BimProject, BimModel
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
      return HttpResponseRedirect('/admin')
  else:
    form = AddBimModelForm()
  context = {'form': form, 'project': project}
  return render(request, 'projects/add_bim_model.html', context)
