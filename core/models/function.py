from django.db import models
from .position import Position
from usuario.models import Usuario as User
from .sector import Sector

class Function(models.Model):
    employer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='employer')
    supervisor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='supervisor')
    position = models.ForeignKey(Position, on_delete=models.PROTECT, related_name='position')
    initial_date = models.DateField(auto_now_add=True)
    final_date = models.DateField(null=True, blank=True)
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT, default=None)
 

    def __str__(self):
        return f'{self.employer.registration} - {self.supervisor.registration}'
    
    class Meta:
        verbose_name = 'function'
        verbose_name_plural = 'functions'