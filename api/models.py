from django.db import models

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=255)
    #description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(auto_now_add=True)
