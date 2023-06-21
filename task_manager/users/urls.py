from django.urls import path
from task_manager.users import views


urlpatterns = [
    path('', views.Users.as_view(), name='user_list'),
    path('create/', views.CreateUser.as_view(), name='create_user'),
    # path('<int:pk>/update/', views.UpdateUser.as_view(), name='update_user'),
    # path('<int:pk>/delete/', views.DeleteUser.as_view(), name='delete_user'),
]
