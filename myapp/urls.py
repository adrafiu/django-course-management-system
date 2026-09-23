from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('students/', views.student_list, name='student_list'), 
    path('students/create/', views.student_create, name='student_create'), 
    path('students/update/<int:id>/', views.student_update, name='student_update'), 
    path('students/delete/<int:id>/', views.student_delete, name='student_delete'),
    path('results/', views.result_list, name='result_list'), 
    path('results/create/', views.result_create, name='result_create'), 
    path('results/update/<int:id>/', views.result_update, name='result_update'), 
    path('results/delete/<int:id>/', views.result_delete, name='result_delete'),

 

] 