from random import choice

from rest_framework import viewsets, views
from rest_framework.response import Response

from words.models import Word
from api.serializers import WordSerializer, StudySerializer
from api.permissions import IsOwner


class WordViewSet(viewsets.ModelViewSet):
    serializer_class = WordSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Word.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StudyView(views.APIView):
    permission_classes = [IsOwner]

    def get(self, request):
        words = Word.objects.filter(owner=request.user)
        word = choice(words)
        return Response(StudySerializer(word).data)

    def post(self, request):
        word = Word.objects.get(id=request.data["id"])
        result = "correct" if word.word == request.data["word"] else "incorrect"
        return Response({"result": result})
