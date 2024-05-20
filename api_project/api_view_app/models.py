from django.db import models

# Create your models here.
class Todo(models.Model):
    todo_title=models.CharField(max_length=20)
    todo_description=models.TextField(max_length=100)
    is_done=models.BooleanField(default=False)
