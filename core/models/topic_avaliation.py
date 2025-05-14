from django.db import models
from .avaliation import Avaliation
from .topic import Topic

class TopicAvaliation(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT, related_name='topic_avaliations')
    avaliation = models.ForeignKey(Avaliation, on_delete=models.PROTECT, related_name='topic_avaliations', null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.topic.title} - {self.avaliation.evaluator.registration}'
    
    class Meta:
        verbose_name = "Topic Avaliation"
        verbose_name_plural = "Topics Avaliations"
        ordering = ['topic']