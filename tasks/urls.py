"""tasks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo.views import TaskListView, AddTaskView, ListTasks, SpecificTask, RegisterUserView
from todo import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
app_name = 'tasks'
urlpatterns = [
    path('admin/', admin.site.urls),
    # Api views
    path('tasks/', ListTasks.as_view(), name="tasks"),
    path('login_api/', obtain_auth_token, name="login"),
    path('tasks/<int:id>/', SpecificTask.as_view(), name="specific_task"),
    # Templates views
    path('', TaskListView.as_view(), name='index'),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("new/", AddTaskView.as_view(), name="new"),
]
# imp for what you want to achieve.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
