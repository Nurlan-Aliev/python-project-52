from django.urls import path
from task_manager.statuses import views


urlpatterns = [
    path('', views.StatusesView.as_view(), name='status_list'),
    path('create/', views.CreateStatusesView.as_view(), name='create_status'),
    path('<int:pk>/update/', views.UpdateStatusesView.as_view(), name='update_status'),
    path('<int:pk>/delete/', views.DeleteStatusesView.as_view(), name='delete_status'),
]
