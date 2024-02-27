from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView

from .models import BimProject
from .mixins import StaffMixin

# Create your views here.

class CreateBimProject(StaffMixin, CreateView):
  model = BimProject
  fields = '__all__'
  template_name = 'projects/create_project.html'
  success_url = '/'

def manage_project_view(request, pk):
  project = get_object_or_404(BimProject, pk=pk)
  context = {'project': project}
  return render(request, 'projects/manage_project.html', context)