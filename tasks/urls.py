from django.urls import path
from . import views


urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('<int:task_id>/toggle_status/', views.toggle_task_status, name='toggle_status'),
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    path('<int:task_id>/edit/', views.TaskUpdateView.as_view(), name='task_update'),
    path('<int:task_id>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
]