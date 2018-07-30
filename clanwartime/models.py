from django.db import models


class warlist(models.Model):
    warstartT = models.CharField(max_length=50)
    warmsg = models.CharField(max_length=30)
    ctime = models.DateTimeField(auto_now=True)
