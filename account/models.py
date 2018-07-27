
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    identify_clan = models.CharField(max_length=30)
    clanname = models.CharField(max_length=30)
    collect = models.CharField(max_length=30)



