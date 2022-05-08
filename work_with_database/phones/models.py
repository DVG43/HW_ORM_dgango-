from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=150)
    prise = models.FloatField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slag = models.SlugField(max_length=150, db_column=name)
    pass






