from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculated_addresses/', views.calculated, name='calculated_addresses'),
    path('use_distance/', views.use_distance, name='use_distance'),
    path('calculated_distance/', views.calculated_distance, name='calculated_distance'),
]
