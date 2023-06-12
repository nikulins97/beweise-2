from rest_framework import serializers


# Сериализатор данных из БД
class QuestionSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    question = serializers.CharField(max_length=255)
    answer = serializers.CharField(max_length=100)
    created_at = serializers.CharField(max_length=100)


