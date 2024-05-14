from django.urls import path
from . import views

urlpatterns = [
  path('create_project/', views.CreateBimProject.as_view(), name='create_project'),
  path('<int:pk>/', views.ManageBimProject.as_view(), name='manage_project'),
  path('<int:pk>/update_project', views.UpdateBimProject.as_view(), name='update_project'),
  path('<int:pk>/delete_project', views.DeleteBimProject.as_view(), name='delete_project'),
  path('<int:pk>/create_bim_model/', views.CreateBimModel.as_view(), name='create_bim_model'),

  path('models/<int:pk>/', views.ManageBimModel.as_view(), name='manage_bim_model'),
  path('models/<int:pk>/update_model', views.UpdateBimModel.as_view(), name='update_model'),
  path('models/<int:pk>/delete_model', views.DeleteBimModel.as_view(), name='delete_model'),
  path('models/<int:pk>/create_info_sheet/<str:sheet_type>', views.CreateInfoSheet.as_view(), name='create_info_sheet'),
  path('models/<int:pk>/default_info_sheet/<str:sheet_type>', views.DefaultInfoSheet.as_view(), name='default_info_sheet'),

  path('info_sheets/<int:pk>/', views.ManageInfoSheet.as_view(), name='manage_info_sheet'),
  path('info_sheets/<int:pk>/update_info_sheet', views.UpdateInfoSheet.as_view(), name='update_info_sheet'),
  path('info_sheets/<int:pk>/delete_info_sheet', views.DeleteInfoSheet.as_view(), name='delete_info_sheet'),
  path('info_sheets/<int:pk>/create_report', views.CreateReport.as_view(), name='create_report'),
  
  path('reports/<int:pk>/', views.ManageReport.as_view(), name='manage_report'),
  path('reports/<int:pk>/update_report', views.UpdateReport.as_view(), name='update_report'),
  path('reports/<int:pk>/delete_report', views.DeleteReport.as_view(), name='delete_report'),
  path('reports/<int:pk>/create_clash_test', views.CreateClashTest.as_view(), name='create_clash_test'),  
  path('reports/<int:pk>/create_validation_test', views.CreateValidationTest.as_view(), name='create_validation_test'),
  path('reports/<int:id>/update_clash_test/<int:pk>', views.UpdateClashTest.as_view(), name='update_clash_test'),
  path('reports/<int:id>/delete_clash_test/<int:pk>', views.DeleteClashTest.as_view(), name='delete_clash_test'),
  path('reports/<int:id>/update_validation_test/<int:pk>', views.UpdateValidationTest.as_view(), name='update_validation_test'),
  path('reports/<int:id>/delete_validation_test/<int:pk>', views.DeleteValidationTest.as_view(), name='delete_validation_test'), 
  
  path('export/<int:pk>/<str:export_type>', views.BimDataExporter.as_view(), name='export_data'),

  path('import/<int:pk>/<str:import_type>', views.BimDataImporter.as_view(), name='import_data'),

]