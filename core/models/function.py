from django.db import models
from usuario.models import Employer
from .position import Position
from .sector import Sector

class Function(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.PROTECT, related_name='functions')
    supervisor = models.ForeignKey(Employer, on_delete=models.PROTECT, related_name='employers')
    position = models.ForeignKey(Position, on_delete=models.PROTECT, related_name='+')
    initial_date = models.DateField(auto_now_add=True)
    final_date = models.DateField(null=True, blank=True)
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT, default=None)

    def __str__(self):
        return f'{self.employer.registration} - {self.supervisor.registration}'
    
    class Meta:
        verbose_name = 'function'
        verbose_name_plural = 'functions'