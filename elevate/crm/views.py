from django.shortcuts import render, redirect
from .models import Task

from .forms import TaskForm, CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate


def homepage(request):

    return render(request, 'crm/index.html')


def task(request):

    queryDataAll = Task.objects.all()

    context = {'AllTask': queryDataAll}

    return render(request, 'crm/task.html', context)


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('my-login')

    context = {'RegistrationForm': form}
    return render(request, 'crm/register.html', context)


def task_form(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('task')

    context = {'form': form}
    return render(request, 'crm/task-form.html', context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('task')

    context = {'updateTask': form}

    return render(request, 'crm/update-task.html', context)


def delete_task(request, pk):

    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('task')

    return render(request, 'crm/delete-task.html')


def my_login(request):

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")

    context = {'LoginForms': form}

    return render(request, 'crm/my-login.html', context)

@login_required(login_url='my-login')
def dashboard(request):

    return render(request, 'crm/dashboard.html')


def log_out(request):
    auth.logout(request)
    return redirect('')
