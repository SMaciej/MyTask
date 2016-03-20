# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITIES = ((1, 'Niski'),(2, 'Normalny'),(3, 'Wysoki'),)

    name = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    priority = models.IntegerField(default=2, choices=PRIORITIES)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.name.encode('utf-8')

