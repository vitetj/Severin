from django.db import models

#class Offer(models.Model):
#    type = models.ForeignKey(
#                'production.Manufacturer',
#                on_delete=models.CASCADE,
#           )
class Vps(models.Model):
    name = models.CharField(max_length = 100)
    ram = models.IntegerField()
    storage = models.IntegerField()
    storageType = models.CharField(max_length = 100)
    traffic = models.IntegerField()
    cost = models.IntegerField(default=0)
    option = models.TextField(blank=True)
    active = models.BooleanField(default=True)


class Web(models.Model):
    name = models.CharField(max_length = 100)
    storage = models.IntegerField()
    storageBackup = models.IntegerField()
    nbSite = models.IntegerField()
    traffic = models.IntegerField()
    cost = models.IntegerField(default=0)
    option = models.TextField(blank=True)
    active = models.BooleanField(default=True)


class Mail(models.Model):
    nbComptes = models.IntegerField()
