# beweise-2
Тестовое задание, задача 2.

Сервис выполнен на основе Django, Django REST Framework. В качестве СУБД использутся PostgreSQL.

Для запуска контейнера в терминале из директории drf_api выполнить команду: docker compose up --detach

Для добавления вопросов для викторины в БД отправить POST-запрос на url http://localhost:8000/number/. Пример запроса: {"questions_num": 1}.

Сервис возвращает предыдущий сохранённый вопрос для викторины (если вопрос отсутствует - пустой объект).
