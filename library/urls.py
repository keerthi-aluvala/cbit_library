from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='library-home'),
    path('it_sems/', views.it_sems, name='library-it-sems'),
    path('cse_sems/', views.cse_sems, name='library-cse-sems'),
    path('ece_sems/', views.ece_sems, name='library-ece-sems'),
    path('eee_sems/', views.eee_sems, name='library-eee-sems'), 
    path('it_sem3/', views.it_sem3, name='library-it-sem3'), 

]
