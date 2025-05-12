from django.db import models
from usuario.models import Usuario as User

class Avaliation(models.Model):
    evaluated = models.ForeignKey(User, on_delete=models.PROTECT, related_name='evaluated')
    evaluator = models.ForeignKey(User, on_delete=models.PROTECT, related_name='evaluators')
    evaluation_date = models.DateField(auto_now_add=True)
    next_evaluation_date = models.DateField(null=True, blank=True)
    strengths = models.TextField(null=True, blank=True)
    weaknesses = models.TextField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.evaluated.registration} - {self.evaluator.registration}'
    
    class Meta:
        verbose_name = "Avaliation"
        verbose_name_plural = "Avaliations"
        ordering = ['-evaluation_date']