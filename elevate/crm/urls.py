from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name=""),
    path('register', views.register, name="register"),
    path('task', views.task, name="task"),
    path('task-form', views.task_form, name="task-form"),
    path('update-task/<str:pk>', views.update_task, name="update-task"),
    path('delete-task/<str:pk>', views.delete_task, name="delete-task"),
    path('my-login', views.my_login, name="my-login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('log-out', views.log_out, name="log-out"),
]

