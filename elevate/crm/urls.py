from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name="home"),
    path('register', views.register, name="register"),
    path('task', views.task, name="task"),
    path('task-form', views.task_form, name="task-form"),
    path('update-task/<str:pk>', views.update_task, name="update-task"),
    path('delete-task/<str:pk>', views.delete_task, name="delete-task"),
]

