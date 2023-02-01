from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Task, SubtaskModel


class loginform(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'Status', 'owner']


class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubtaskModel
        fields = ['subtask_name', 'task_id']
