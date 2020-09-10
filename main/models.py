from django.db import models
from django.contrib.auth.models import User
# Used to generate urls by reversing the URL patterns
from django.urls import reverse
from django.db.models.signals import post_save
from django.core.validators import MinValueValidator, MaxValueValidator
#relation containg all genre of books


class takenCourses(models.Model):

	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class grading(models.Model):
    grades = models.ForeignKey(takenCourses, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=5)
    interest = models.IntegerField(default = 1, validators=[MaxValueValidator(10), MinValueValidator(0)])

    def __str__(self):
        return self.grades


class suggestCourses(models.Model):

	course = models.CharField(max_length=200)

	def __str__(self):
		return self.course


class interest(models.Model):
    interest = models.ForeignKey(takenCourses, on_delete=models.CASCADE)

    interest = models.IntegerField( default=1, validators=[MaxValueValidator(10), MinValueValidator(0)])

    def __str__(self):
        return self.interest
