from django.db import models
from django.urls import reverse


# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = "известные певицы"
        verbose_name_plural = "известные певицы"

    def get_absolute_url(self):
        return reverse('womenslug', kwargs={'sl': self.slug})


class TheBestBooks(models.Model):
    BooksName = models.CharField(max_length=40)
    Author = models.CharField(max_length=15)
    DateOfBirth = models.CharField(max_length=10)
    Summary = models.TextField(blank=True)
    Cost = models.IntegerField(default=700)
    Interest = models.BooleanField(default=True)

    class Meta:
        verbose_name = "мои любимые книги"
        verbose_name_plural = "мои любимые книги"
