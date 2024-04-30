from django.urls import path

from . import views

urlpatterns = [
    path('', views.OrganizationSettings.as_view(), name='organization_settings'),

    path('create_phase/', views.CreateProjectPhase.as_view(), name='create_phase'),
    path('update_phase/<int:pk>', views.UpdateProjectPhase.as_view(), name='update_phase'),
    path('delete_phase/<int:pk>', views.DeleteProjectPhase.as_view(), name='delete_phase'),
]

