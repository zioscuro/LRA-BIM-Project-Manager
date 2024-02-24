from django.urls import path

from .views import homepage, user_profile_view

urlpatterns = [
    path('', homepage, name='homepage'),
    path('user/<str:username>/', user_profile_view, name='user_profile'), 
]
