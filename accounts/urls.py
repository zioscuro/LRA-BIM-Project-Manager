from django.urls import path

from accounts.views import create_account_view

urlpatterns = [
    path('create_account/', create_account_view, name='create_account_view'),    
]