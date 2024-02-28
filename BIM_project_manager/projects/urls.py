from django.urls import path
from .views import CreateBimProject, manage_project_view, add_bim_model_view, manage_bim_model_view

urlpatterns = [
  path('new_project/', CreateBimProject.as_view(), name='create_project'),
  path('manage_project/<int:pk>/', manage_project_view, name='manage_project'),
  path('manage_project/<int:pk>/add_model/', add_bim_model_view, name='add_bim_model'),
  path('manage_model/<int:pk>/', manage_bim_model_view, name='manage_bim_model'),
]