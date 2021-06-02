from django.urls import path
from .import views

urlpatterns = [
    path('register_login',views.index),
    path('register',views.register),
    path('login',views.login)
]