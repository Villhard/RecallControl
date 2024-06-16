from rest_framework import viewsets

from words.models import Word
from api.serializers import WordSerializer
from api.permissions import IsOwner


class WordViewSet(viewsets.ModelViewSet):
    serializer_class = WordSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Word.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
