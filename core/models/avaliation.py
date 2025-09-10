from django.db import models
from usuario.models import Usuario as User
from django.db.models.signals import post_save
from django.dispatch import receiver
from email_alternatives.send_email_to_evaluted import send_email_to_evaluated
from datetime import date


class Avaliation(models.Model):
    evaluated = models.ForeignKey(User, on_delete=models.PROTECT, related_name='evaluated')
    evaluator = models.ForeignKey(User, on_delete=models.PROTECT, related_name='evaluators')
    evaluation_date = models.DateField(auto_now_add=True)
    next_evaluation_date = models.DateField(null=True, blank=True)
    strengths = models.TextField(null=True, blank=True)
    weaknesses = models.TextField(null=True, blank=True)
    score = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return f'{self.evaluated.registration} - {self.evaluator.registration}'
    
    class Meta:
        verbose_name = "Avaliation"
        verbose_name_plural = "Avaliations"
        ordering = ['-evaluation_date']
    
    @property
    def avaliation_is_in_day(self):
       return date.today() >= self.next_evaluation_date
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = self.evaluated
        user_avaliation = Avaliation.objects.filter(evaluated=user)

        if user_avaliation.exists():
            user.media = sum(sco.score for sco in user_avaliation) / len(user_avaliation)
        else:
            user.media = 0 

        user.save(update_fields=["media"]) 

        return super().save(force_insert, force_update, using, update_fields)

@receiver(post_save, sender=Avaliation)
def send_email_after_evaluated_receive_score(instance, created, sender, **kwargs):
    if created: 
        send_email_to_evaluated(evaluated=instance.evaluated, evaluator=instance.evaluator, score=instance.score)
    
        

    