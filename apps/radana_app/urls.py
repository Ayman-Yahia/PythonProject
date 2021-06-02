from django.urls import path
from .import views

urlpatterns = [
    path('',views.index),
    path('ajax_calls/search/', views.autocompleteModel),

    
]