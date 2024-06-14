from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=100)
    definition = models.TextField()
    example = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    learned_at = models.DateTimeField(null=True, blank=True)
