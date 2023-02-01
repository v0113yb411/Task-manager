from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import TaskForm, SubTaskForm, loginform
from django.contrib.auth import login, logout, authenticate
from .models import Task, SubtaskModel, Task
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.middleware import AuthenticationMiddleware
# Create your views here.


def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'GET':
        form = loginform()
        return render(request, 'login.html', {'form': form})

    if request.method == 'POST':
        print('You are in post of login')
        form = loginform(request.POST, data=request.POST)
        if form.is_valid():
            print('Validated')
            uname = form.cleaned_data['username']
            pword = form.cleaned_data['password']
            user = authenticate(username=uname, password=pword)
            print(user)
            if user is not None:
                login(request, user)
                print('user logged in')
                return redirect('task_list')
            return redirect('home')
        return redirect('home')


@login_required
def create_task(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'create_task.html', {'form': form})

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')


@login_required
def task_detail(request, pk):
    if request.method == 'GET':
        task_data = Task.objects.get(id=pk)
        print(task_data)
        sub_task_data = SubtaskModel.objects.filter(task_id=pk)
        sub_task_form = SubTaskForm()
        return render(request, 'task_detail.html', {'data': sub_task_form, 'sub_task_data': sub_task_data, 'task_data': task_data})


@login_required
def task_list(request):
    if request.user.is_authenticated:
        task = Task.objects.filter(owner=request.user.id)
        return render(request, 'task_list.html', {'tasks': task})
    else:
        return HttpResponse('You are not allowed to enter here.')


def log_out(request):
    if request.method == 'GET':
        logout(request)
        messages.warning(request, 'logged out successfuly !!!')
        return redirect('home')


@login_required
def add_sub_task(request):
    if request.method == 'POST':
        form = SubTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')


@login_required
def delete_task(request, pk):
    data = Task.objects.get(id=pk)
    print(data)
    data.delete()
    return redirect('task_list')


@login_required
def edit_task(request, pk):
    if request.method == 'GET':
        status = Task.STATUS_CHOICES
        print(status)
        task = Task.objects.get(id=pk)
        print(task)
        return render(request, 'edit_task.html', {'status': status, 'task': task})

    if request.method == 'POST':
        tname = request.POST['task_name']
        sname = request.POST['Status']
        print(sname)
        current_user = User.objects.get(id=request.user.id)
        owner = request.user.id
        user = Task.objects.get(id=pk)
        user.task_name = tname
        user.Status = sname
        user.owner = current_user
        user.save()
        return redirect('task_list')
