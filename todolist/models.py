from datetime import date

from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class ToDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    is_complete = models.BooleanField('Завершено', default=False)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title

