from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Product(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(
        max_length=1000,
        blank=True,
        null=True
    )


class Plan(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(
        max_length=1000,
        blank=True,
        null=True
    )
    cycle = models.CharField(
        max_length=24,
        choices=(
            ('m', 'Monthly'),
            ('a', 'Annual'),
            ('o', 'One Time')
        )
    )
    price = models.IntegerField()
