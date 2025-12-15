from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Статическая страница'
        verbose_name_plural = 'Статические страницы'

    def __str__(self):
        return self.title
