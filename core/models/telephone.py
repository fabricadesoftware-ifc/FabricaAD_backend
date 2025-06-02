from django.db import models
from usuario.models import Usuario as User
from .enterprise import Enterprise

class Telephone(models.Model):
    number = models.CharField(max_length=9, blank=False, null=False)
    type = models.CharField(max_length=45, blank=True, null=True)
    user_phone = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, default=None, related_name='telephones')
    enterprise_phone = models.ForeignKey(Enterprise, on_delete=models.PROTECT, null=True, blank=True, default=None)

    def __str__(self):
        return self.number
    
    class Meta:
        verbose_name = 'telephone'
        verbose_name_plural = 'telephones'
        
    
