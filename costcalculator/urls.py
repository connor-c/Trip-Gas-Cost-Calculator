from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculated/', views.calculated, name='calculated'),
]
