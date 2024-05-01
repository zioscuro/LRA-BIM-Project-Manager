from django.urls import path

from . import views

urlpatterns = [
    path('', views.OrganizationSettings.as_view(), name='organization_settings'),

    path('create_phase/', views.CreateProjectPhase.as_view(), name='create_phase'),
    path('update_phase/<int:pk>', views.UpdateProjectPhase.as_view(), name='update_phase'),
    path('delete_phase/<int:pk>', views.DeleteProjectPhase.as_view(), name='delete_phase'),

    path('create_discipline/', views.CreateDiscipline.as_view(), name='create_discipline'),
    path('update_discipline/<int:pk>', views.UpdateDiscipline.as_view(), name='update_discipline'),
    path('delete_discipline/<int:pk>', views.DeleteDiscipline.as_view(), name='delete_discipline'),
]

