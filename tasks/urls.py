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
from todo.views import TaskListView
from todo import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'tasks'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', views.task_list),
    path('tasks/<int:id>/', views.task_detail),
    path('', TaskListView.as_view(), name='index'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
]
# imp for what you want to achieve.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
