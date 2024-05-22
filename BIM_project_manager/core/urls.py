from django.urls import path
from .views import HomeView, UserList, user_profile_view

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('users/', UserList.as_view() , name='user_list'),
    path('user/<str:username>/', user_profile_view, name='user_profile'),
]
