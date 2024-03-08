from django.urls import path
from . import views

urlpatterns = [
  path('new_project/', views.CreateBimProject.as_view(), name='create_project'),
  path('manage_project/<int:pk>/', views.manage_project_view, name='manage_project'),
  path('manage_project/<int:pk>/update_project', views.UpdateBimProject.as_view(), name='update_project'),
  path('manage_project/<int:pk>/delete_project', views.DeleteBimProject.as_view(), name='delete_project'),
  path('manage_project/<int:pk>/add_model/', views.add_bim_model_view, name='add_bim_model'),
  path('manage_project/<int:pk>/export_model_register/', views.export_model_register, name='export_model_register'),
  path('manage_project/<int:pk>/export_project_info_sheets/', views.export_project_info_sheets, name='export_project_info_sheets'),

  path('manage_model/<int:pk>/', views.manage_bim_model_view, name='manage_bim_model'),
  path('manage_model/<int:pk>/update_model', views.UpdateBimModel.as_view(), name='update_model'),
  path('manage_model/<int:pk>/delete_model', views.DeleteBimModel.as_view(), name='delete_model'),
  path('manage_model/<int:pk>/add_info_sheet/<str:sheet_type>', views.add_info_sheet_view, name='add_info_sheet'),
  path('manage_model/<int:pk>/default_coordination', views.default_coordination, name='default_coordination'),
  path('manage_model/<int:pk>/default_validation', views.default_validation, name='default_validation'),
  path('manage_model/<int:pk>/export_model_info_sheets', views.export_model_info_sheets, name='export_model_info_sheets'),

  path('manage_info_sheet/<int:pk>/', views.manage_info_sheet_view, name='manage_info_sheet'),
  path('manage_info_sheet/<int:pk>/update_info_sheet', views.UpdateInfoSheet.as_view(), name='update_info_sheet'),
  path('manage_info_sheet/<int:pk>/delete_info_sheet', views.DeleteInfoSheet.as_view(), name='delete_info_sheet'),
  path('manage_info_sheet/<int:pk>/add_report', views.add_report_view, name='add_report'),
  
  path('manage_report/<int:pk>/', views.manage_report_view, name='manage_report'),
  path('manage_report/<int:pk>/update_report', views.UpdateReport.as_view(), name='update_report'),
  path('manage_report/<int:pk>/delete_report', views.DeleteReport.as_view(), name='delete_report'),
  path('manage_report/<int:pk>/add_clash_test', views.add_clash_test_view, name='add_clash_test'),
  path('manage_report/<int:pk>/add_validation_test', views.add_validation_test_view, name='add_validation_test'),
  
  path('update_clash_test/<int:pk>', views.UpdateClashTest.as_view(), name='update_clash_test'),
  path('update_validation_test/<int:pk>', views.UpdateValidationTest.as_view(), name='update_validation_test'),
  path('delete_clash_test/<int:pk>', views.DeleteClashTest.as_view(), name='delete_clash_test'),
  path('delete_validation_test/<int:pk>', views.DeleteValidationTest.as_view(), name='delete_validation_test'),

]