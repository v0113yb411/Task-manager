from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    task_name = models.CharField(max_length=100)
    STATUS_CHOICES = (
        (1, 'Not Started'),
        (2, 'In Progress'),
        (3, 'Completed'),
    )
    Status = models.IntegerField(choices=STATUS_CHOICES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.task_name


class SubtaskModel(models.Model):
    subtask_name = models.CharField(max_length=100)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.subtask_name
