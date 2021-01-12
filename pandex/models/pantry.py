from django.db import models
from django.contrib.auth.models import Group


class Pantry(models.Model):
    name = models.CharField(max_length=200)
    group = models.OneToOneField(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
