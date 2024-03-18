from django.db import models
from django.utils.text import slugify


class Library(models.Model):

    display_heading = models.CharField(max_length=100, verbose_name='Отображаемый заголовок', null=True)
    heading = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    style = models.TextField()
    year_of_publication = models.DateTimeField()


    slug = models.SlugField(unique=True,allow_unicode=True, verbose_name='Slug')



    def save(self, *args, **kwargs):
        self.slug = slugify(self.heading)
        super().save(*args, **kwargs)

    def __str__(self,):
        return f'книга {self.heading}'

