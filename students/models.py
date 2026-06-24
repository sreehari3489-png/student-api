from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    course = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    joined_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
