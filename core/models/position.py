from django.db import models

class Position(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'position'
        verbose_name_plural = 'positions'