from django.db import models
from .enterprise import Enterprise

class Topic(models.Model):
    title = models.CharField(max_length=45, blank=False, null=False)
    enterprise_topic = models.ForeignKey(Enterprise, on_delete=models.PROTECT, null=True, blank=True, default=None)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = "Topics"
        ordering = ['title']