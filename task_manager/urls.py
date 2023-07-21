from django.contrib import admin
from django.urls import path, include
from task_manager import view


urlpatterns = [
    path('', view.HomePageViews.as_view(), name='home_page'),
    path('users/', include('task_manager.users.urls')),
    path('statuses/', include('task_manager.statuses.urls')),
    path('tasks/', include('task_manager.tasks.urls')),
    path('labels/', include('task_manager.labels.urls')),
    path('login/', view.LoginUser.as_view(), name='login'),
    path('logout/', view.LogoutUser.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
