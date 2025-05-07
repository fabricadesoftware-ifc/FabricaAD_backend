from django.db import models
from .enterprise import Enterprise

class Sector(models.Model):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.PROTECT, related_name='sectors')
    name = models.CharField(max_length=40, blank=False, null=False, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sector"
        verbose_name_plural = "Sectors"