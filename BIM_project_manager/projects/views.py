from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import BimProject
from .mixins import StaffMixin

# Create your views here.

class CreateBimProject(StaffMixin, CreateView):
  model = BimProject
  fields = '__all__'
  template_name = 'projects/create_project.html'
  success_url = '/'