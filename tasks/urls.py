from django.urls import path 
from tasks import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', views.create_task, name = 'create_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
]

#sem o <int:task_id> o Django não sabia que a URL tinha um número variável!