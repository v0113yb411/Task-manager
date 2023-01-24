from django.urls import path, include
from .import views


urlpatterns = [
    path("", views.home, name='home'),
    path("login/", views.login_view, name='login'),
    path("create_task/", views.create_task, name='create_task'),
    path("add_sub_task/", views.add_sub_task, name='add_sub_task'),
    path("task_list/", views.task_list, name='task_list'),
    path("create_task/", views.create_task, name='create_task'),
    path("task_detail/<int:pk>", views.task_detail, name='task_detail'),
    path('edit_task/<int:pk>', views.edit_task, name='edit_task'),
    path('delete_task/<int:pk>', views.delete_task, name='delete_task'),




]
