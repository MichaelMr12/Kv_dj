from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


# def translit_to_eng(s: str) -> str:
#     d = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
#          'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'к': 'k',
#          'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
#          'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
#          'ш': 'sh', 'щ': 'shch', 'ь': '', 'ы': 'y', 'ъ': '', 'э': 'r', 'ю': 'yu', 'я': 'ya'}
#
#     return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))

# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    content = models.TextField(blank=True, verbose_name='подробно')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='время обновления')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = "известные певицы"
        verbose_name_plural = "известные певицы"

    def get_absolute_url(self):
        return reverse('womenslug', kwargs={'sl': self.slug})
    # def save(self,*args,**kwargs):
    #     self.slug = slugify(translit_to_eng(self.title))
    #     super().save(*args,**kwargs)


class TheBestBooks(models.Model):
    BooksName = models.CharField(max_length=40, verbose_name='название книги')
    Author = models.CharField(max_length=15, verbose_name='автор')
    DateOfBirth = models.CharField(max_length=10, verbose_name='дата рождения автора')
    Summary = models.TextField(blank=True, verbose_name='объем')
    Cost = models.IntegerField(default=700, verbose_name='стоимость')
    Interest = models.BooleanField(default=True, verbose_name='👌👌')

    class Meta:
        verbose_name = "мои любимые книги"
        verbose_name_plural = "мои любимые книги"
