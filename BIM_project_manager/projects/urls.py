from django.urls import path
from . import views

urlpatterns = [
  path('new_project/', views.CreateBimProject.as_view(), name='create_project'),
  path('manage_project/<int:pk>/', views.manage_project_view, name='manage_project'),
  path('manage_project/<int:pk>/add_model/', views.add_bim_model_view, name='add_bim_model'),
  path('manage_model/<int:pk>/', views.manage_bim_model_view, name='manage_bim_model'),
  path('manage_model/<int:pk>/add_info_sheet/<str:sheet_type>', views.add_info_sheet_view, name='add_info_sheet'),
  path('manage_info_sheet/<int:pk>/', views.manage_info_sheet_view, name='manage_info_sheet'),
  path('manage_info_sheet/<int:pk>/add_info_sheet', views.add_report_view, name='add_report'),
  path('manage_report/<int:pk>/', views.manage_report_view, name='manage_report'),
  path('manage_report/<int:pk>/add_clash_test', views.add_clash_test_view, name='add_clash_test'),
  path('manage_report/<int:pk>/add_validation_test', views.add_validation_test_view, name='add_validation_test'),
]