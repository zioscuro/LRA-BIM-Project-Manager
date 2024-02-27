from django.urls import path

from .views import HomeView, user_profile_view, UserList

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('users/', UserList.as_view() , name='user_list'),
    path('user/<str:username>/', user_profile_view, name='user_profile'), 
]
