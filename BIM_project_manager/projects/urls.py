from django.urls import path
from .views import CreateBimProject, manage_project_view

urlpatterns = [
  path('new_project/', CreateBimProject.as_view(), name='create_project'),
  path('manage_project/<int:pk>', manage_project_view, name='manage_project'),
]