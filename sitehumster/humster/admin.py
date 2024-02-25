from django.contrib import admin

from .models import Women, TheBestBooks

# Register your models here.
@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ['title', 'slug','content', 'is_published']
    #readonly_fields = ['slug']
    prepopulated_fields = {"slug":("title",)}
    list_display = ('id', 'title', 'slug', 'content','time_create', 'is_published')
    list_display_links = ('id', )
    list_editable = ('title',)
#admin.site.register(TheBestBooks)

@admin.register(TheBestBooks)
class TheBestBooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'Author', 'BooksName','DateOfBirth', 'Interest')
    list_display_links = ('id', )
    list_editable = ('BooksName',)