from django.db import models

# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

class TheBestBooks(models.Model):
    BooksName = models.CharField(max_length=40)
    Author = models.CharField(max_length=15)
    DateOfBirth = models.CharField(max_length=10)
    Summary = models.TextField(blank=True)
    Cost = models.IntegerField(default=700)
    Interest = models.BooleanField(default=True)