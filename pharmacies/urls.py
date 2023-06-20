from . import views
from django.urls import path

urlpatterns = [
    path('loginuser/', views.loginuser, name='login')
]