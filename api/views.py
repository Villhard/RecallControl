from rest_framework import viewsets

from words.models import Word
from api.serializers import WordSerializer


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
