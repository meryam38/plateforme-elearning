from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Champs supplémentaires pour les utilisateurs

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Champs supplémentaires pour les cours

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    # Champs supplémentaires pour les leçons