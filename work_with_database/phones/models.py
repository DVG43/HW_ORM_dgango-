from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=150)
    image = models.ImageField()
    prise = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slag = models.SlugField()
    pass

#max_length=150, name=slugify(name)




