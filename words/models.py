from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Word(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="words")
    word = models.CharField(max_length=100)
    definition = models.TextField()
    example = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    learned_at = models.DateTimeField(null=True, blank=True)
