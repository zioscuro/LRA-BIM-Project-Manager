from django.urls import path
from projects import views

urlpatterns = [
  path('create_bim_project', views.CreateBimProject.as_view(), name='create_bim_project'),
  path('manage_bim_project/<int:pk>', views.ManageBimProject.as_view(), name='manage_bim_project'),
  path('manage_bim_project/<int:pk>/create_bim_model', views.CreateBimModel.as_view(), name='create_bim_model'),
  path('update_bim_project/<int:pk>', views.UpdateBimProject.as_view(), name='update_bim_project'),
  path('delete_bim_project/<int:pk>', views.DeleteBimProject.as_view(), name='delete_bim_project'),

  path('manage_bim_model/<int:pk>', views.ManageBimModel.as_view(), name='manage_bim_model'),
  path('manage_bim_model/<int:pk>/create_info_sheet/<str:sheet_type>', views.CreateInfoSheet.as_view(), name='create_info_sheet'),
  path('manage_bim_model/<int:pk>/default_info_sheet/<str:sheet_type>', views.DefaultInfoSheet.as_view(), name='default_info_sheet'),
  path('update_bim_model/<int:pk>', views.UpdateBimModel.as_view(), name='update_bim_model'),
  path('delete_bim_model/<int:pk>', views.DeleteBimModel.as_view(), name='delete_bim_model'),

  path('manage_info_sheet/<int:pk>', views.ManageInfoSheet.as_view(), name='manage_info_sheet'),
  path('manage_info_sheet/<int:pk>/create_report', views.CreateReport.as_view(), name='create_report'),
  path('update_info_sheet/<int:pk>', views.UpdateInfoSheet.as_view(), name='update_info_sheet'),
  path('delete_info_sheet/<int:pk>', views.DeleteInfoSheet.as_view(), name='delete_info_sheet'),
  
  path('manage_report/<int:pk>/', views.ManageReport.as_view(), name='manage_report'),
  path('manage_report/<int:pk>/update_report', views.UpdateReport.as_view(), name='update_report'),
  path('manage_report/<int:pk>/delete_report', views.DeleteReport.as_view(), name='delete_report'),
  path('manage_report/<int:pk>/create_clash_test', views.CreateClashTest.as_view(), name='create_clash_test'),  
  path('manage_report/<int:pk>/create_validation_test', views.CreateValidationTest.as_view(), name='create_validation_test'),
  path('manage_report/<int:id>/update_clash_test/<int:pk>', views.UpdateClashTest.as_view(), name='update_clash_test'),
  path('manage_report/<int:id>/delete_clash_test/<int:pk>', views.DeleteClashTest.as_view(), name='delete_clash_test'),
  path('manage_report/<int:id>/update_validation_test/<int:pk>', views.UpdateValidationTest.as_view(), name='update_validation_test'),
  path('manage_report/<int:id>/delete_validation_test/<int:pk>', views.DeleteValidationTest.as_view(), name='delete_validation_test'), 
  
  path('export_bim_data/<int:pk>/<str:export_type>', views.BimDataExporter.as_view(), name='export_bim_data'),
  path('import_bim_data/<int:pk>/<str:import_type>', views.BimDataImporter.as_view(), name='import_bim_data'),
]
