from django.urls import path
from task_manager.tasks import views


urlpatterns = [
    path('', views.TaskView.as_view(), name='task_list'),
    path('', views.CreateTaskView.as_view(), name='task_list'),
    path('', views.UpdateTaskView.as_view(), name='task_list'),
    path('', views.DeleteTaskView.as_view(), name='task_list'),
    path('', views.TaskView.as_view(), name='task_list'),
]