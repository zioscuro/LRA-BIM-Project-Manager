from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from projects.models import BimProject

# Create your views here.

# def homepage(request):
#   return render(request, 'core/homepage.html')

class HomeView(ListView):
  queryset = BimProject.objects.all()
  template_name = 'core/homepage.html'
  context_object_name = 'BimProjects_list'

def user_profile_view(request, username):
  user = get_object_or_404(User, username=username)
  context = {'user': user}
  return render(request, 'core/user_profile.html', context)

class UserList(ListView):
  model = User
  template_name = 'core/users.html'
  context_object_name = 'Users_list'
  
# class OrganizationSettings(StaffMixin, View):
#   def get(self, request):
#     project_phases = ProjectPhase.objects.all()
#     disciplines = Discipline.objects.all()
#     software_list = AuthoringSoftware.objects.all()
#     lod_list = LodReference.objects.all()
#     specifications_list = BimSpecification.objects.all()
#     expert_list = BimExpert.objects.all()

#     context = {
#       'project_phases': project_phases,
#       'disciplines': disciplines,
#       'software_list': software_list,
#       'lod_list': lod_list,
#       'specifications_list': specifications_list, 
#       'expert_list': expert_list 
#       }

#     return render(request, 'core/organization_settings.html', context)