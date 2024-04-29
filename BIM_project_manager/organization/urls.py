from django.urls import path

from .views import OrganizationSettings

urlpatterns = [
    path('', OrganizationSettings.as_view(), name='organization_settings'),
]

