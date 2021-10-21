from django.db import models
from autoslug import AutoSlugField
import datetime


class Phone(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    image = models.CharField(max_length=255, default='empty')
    release_date = models.DateField(default=datetime.date.today)
    lte_exists = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='name', null=True)

    def __str__(self):
        return f"{self.id}: {self.name}"
