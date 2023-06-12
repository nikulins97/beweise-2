import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import Questions
from app.serializers import QuestionSerializer


# Класс представления для url http://127.0.0.1:8000/number/
class NumberAPIView(APIView):

    # POST-метод
    def post(self, request):

        # Считывание количества запрашиваемых вопросов
        questions_num = request.data['questions_num']

        # Получение последнего сохранённого вопроса из БД
        try:
            last_question = Questions.objects.latest('pk')
        except:
            last_question = None

        # Запрос к публичному API, проверка вопроса на уникальность, занесение в БД
        q = 0
        while not q:
            parsed_list = requests.get(f"https://jservice.io/api/random?count={questions_num}").json()
            for data in parsed_list:
                q = Questions.objects.create(
                    question_id=(data['id']),
                    question=data['question'],
                    answer=data['answer'],
                    created_at=data['created_at']
                )

        # Возврат последнего сохранённого вопроса или пустого объекта (в случае его отсутствия)
        if not last_question:
            return Response(None)

        return Response({'last_saved_question': QuestionSerializer(last_question).data})

