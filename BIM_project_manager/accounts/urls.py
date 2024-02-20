from django.urls import path
from .views import create_account_view

urlpatterns = [
    path('create-account/', create_account_view, name='create_account_view'),    
]