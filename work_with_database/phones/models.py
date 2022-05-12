from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=150)
    prise = models.FloatField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slag = models.SlugField(max_length=150, name = slugify(name))
    pass






