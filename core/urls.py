from django.urls import path
from .views import HomeView, UserList, user_profile_view

urlpatterns = [
    path('', HomeView.as_view(), name=''),
    path('users/', UserList.as_view() , name='users'),
    path('user_profile/<str:username>/', user_profile_view, name='user_profile'),
]
