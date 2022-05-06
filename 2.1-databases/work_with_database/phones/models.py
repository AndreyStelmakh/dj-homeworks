from django.db import models


class Phone(models.Model):
    # id
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.CharField(max_length=250)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=250)
    # TODO: Добавьте требуемые поля
    pass
