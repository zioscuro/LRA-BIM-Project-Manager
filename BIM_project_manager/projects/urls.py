from django.urls import path
from .views import CreateBimProject

urlpatterns = [
  path('new_project/', CreateBimProject.as_view(), name='create_project')
]