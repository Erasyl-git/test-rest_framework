from django.contrib import admin
from .models import Library


class LibraryAdmin(admin.ModelAdmin):
    list_display = ['display_heading', 'author', 'style', 'year_of_publication']


admin.site.register(Library, LibraryAdmin)
