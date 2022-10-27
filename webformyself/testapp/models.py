from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre', kwargs={"pk": self.pk})

    class MPTTMeta:
        order_insertion_by = ['name']


class Article(models.Model):
    name = models.CharField(max_length=50)
    category = TreeForeignKey(Genre, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
