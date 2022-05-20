from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=255)
    image = models.ImageField()
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200, unique=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Phone, self).save(*args, **kwargs)

    pass

#max_length=150, name=slugify(name)




