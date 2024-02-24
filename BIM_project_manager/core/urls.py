from django.urls import path

from .views import homepage, user_profile_view, UserList

urlpatterns = [
    path('', homepage, name='homepage'),
    path('users/', UserList.as_view() , name='user_list'),
    path('user/<str:username>/', user_profile_view, name='user_profile'), 
]
