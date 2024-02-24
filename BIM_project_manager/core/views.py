from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render

# Create your views here.

def homepage(request):
  return render(request, 'core/homepage.html')

def user_profile_view(request, username):
  user = get_object_or_404(User, username=username)
  context = {'user': user}
  return render(request, 'core/user_profile.html', context)
  