from django.db import models

class Telephone(models.Model):
    number = models.CharField(max_length=9, blank=False, null=False)
    type = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.number
    
    class Meta:
        verbose_name = 'telephone'
        
    
