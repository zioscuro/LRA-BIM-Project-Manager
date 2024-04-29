from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from projects.models import BimProject

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
