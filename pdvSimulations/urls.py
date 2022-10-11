from django.urls import path
from . import views

urlpatterns = [
    path('', views.simulations, name='simulations'),
    path('newsimulation/', views.newsimulation, name='newsimulation'),
    path('newitem/', views.newitem, name='newitem'),
]
