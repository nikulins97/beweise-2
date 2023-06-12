from django.db import models


# Класс модели  для БД
class Questions(models.Model):
    question_id = models.IntegerField(unique=True)
    question = models.TextField()
    answer = models.TextField()
    created_at = models.CharField(max_length=100)

    def __str__(self):
        return self.question

