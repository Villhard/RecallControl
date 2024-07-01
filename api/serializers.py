from rest_framework import serializers

from words.models import Word


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ("id", "word", "definition", "example")


class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ("id", "definition", "example")

    def to_representation(self, instance):
        count_letters = len(instance.word)
        example = instance.example.replace(instance.word, "_" * count_letters)
        return {
            "id": instance.id,
            "definition": instance.definition,
            "example": example,
        }
