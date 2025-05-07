from django.db import models
from .usuario import Usuario as User
from uploader.models import Image
from core.models.enterprise import Enterprise

class Employer(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='employers')
    registration = models.CharField(max_length=100, unique=True)
    photo = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='+')
    enterprise = models.ForeignKey(Enterprise, on_delete=models.PROTECT, default=None)

    def __str__(self):
        return self.registration

    class Meta:
        verbose_name = 'employer'
        verbose_name_plural = 'employers'
        ordering = ['-id']
    