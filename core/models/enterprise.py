from django.db import models

class Enterprise(models.Model):
    id_enterprise = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, blank=False, null=False, unique=True)
    fantasy_name = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.fantasy_name
    
    class Meta:
        verbose_name = "enterprise"
        verbose_plural_= "enterprise"