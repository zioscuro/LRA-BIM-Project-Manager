from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from accounts.forms import CreateAccountForm

# Create your views here.
def create_account_view(request):
  if request.method == 'POST':
    form = CreateAccountForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      email = form.cleaned_data['email']
      password = form.cleaned_data['password1']
      User.objects.create_user(username=username, password=password, email=email)
      user = authenticate(username=username, password=password)
      login(request, user)
      return HttpResponseRedirect('/')
  else:
    form = CreateAccountForm()
  context = {'form': form}
  return render(request, 'accounts/create_account.html', context)
