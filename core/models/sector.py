from django.db import models
from django.utils.translation import gettext_lazy as _

class Sector(models.Model):
    id_sector = models.AutoField(primary_key=True)
    enterprise = models.ForeignKey('Enterprise', on_delete=models.PROTECT, related_name='sectors')
    name = models.CharField(max_length=40, blank=False, null=False, unique=True)
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("sector")
        verbose_name_plural = _("sectors")