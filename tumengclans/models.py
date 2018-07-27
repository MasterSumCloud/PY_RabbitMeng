from django.db import models


class TumengClans(models.Model):
    clanname = models.CharField(max_length=50)
    clantag = models.CharField(max_length=30)
    ctime = models.DateTimeField(auto_now=True)
