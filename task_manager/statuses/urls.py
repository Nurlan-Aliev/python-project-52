from django.urls import path
from task_manager.statuses import views


urlpatterns = [
    path('', views.StatusesView.as_view(), name='statuses'),
    path('create/', views.CreateStatusesView.as_view(), name='create_statuses'),
    path('<int:pk>/update/', views.UpdateStatusesView.as_view(), name='update_statuses'),
    path('<int:pk>/delete/', views.DeleteStatusesView.as_view(), name='delete_statuses'),
]
