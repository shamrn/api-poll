
<h3>1 - Запуск локальной версии проекта</h3>
<p>1.1 - git clone</p>
<p>1.2 - pip install -r requirements.txt</p>
<p>1.3 - python manage.py runserver</p>
<hr>
<h3>2 - Gui - стандартная админка Django  </h3>
<hr>
<h3>3 - Работа с api</h3>
<h4>Получение списка активных опросов</h4>
<p>Необходимо отправить get запрос на url - http://127.0.0.1:8000/api/v1/poll-list/ </p>
<p>Ответ:</p>
<p>"id" - уникальный идентификатор опроса
<p>"name" - Название опроса</p>
<p>"desc" - Описание опроса</p>
<p>"start_date" - Дата начала опроса </p>
<p>"end_date" - Дата конца опроса </p>
<br>
<h4>Получить данные конкретного опроса</h4>
<p>Необходимо отправить get запрос на url - http://127.0.0.1:8000/api/v1/take-poll/id/</p>
<p>Где id необходимо указать id - опроса, пример: http://127.0.0.1:8000/api/v1/take-poll/1/</p>
<p>Ответ:</p>
<p>"question" - Список который содержит:</p>
<p>"id" - Уникальный идентификатор вопроса</p>
<p>"desc" - Описание вопроса</p>
<p>"type" - Тип вопроса</p>
<p>"ques_choices" - Список вариантов ответа, который содержит:</p>
<p>"id" - Уникальный идентификатор ответа</p>
<p>"desc" - Описание ответа</p>
<br>
<h4>Отправить данные на сервер, пройденного опроса</h4>
<p>Необходимо отправить post запрос на url - http://127.0.0.1:8000/api/v1/create-answer/</p>
<p>Тело запроса необходимо передавать в формате JSON</p>
<p>Тело запроса содержит:</p>
<p>"user_id" - id пользователя, тип данных int</p>
<p>"poll"- id пройденного опроса, тип данных int</p>
<p>"question" - список с словарями, где ключ является id - вопроса , значение id - ответа/ответов/свой вариант ответа</p>
<p>Пример:"question": [{"1": ["1"]}, {"2": ["3", "4"]}, {"4": ["текст"]}]
<p>Полный пример: {"user_id": 6425400, "poll": 1, "question": [{"1": ["1"]}, {"2": ["3", "4"]}, {"4": ["текст"]}]}
<br>
<h4>Получить данные пройденного опроса</h4>
<p>Необходимо отправить get запрос на url - http://127.0.0.1:8000/api/v1/list-answer/user_id/
<p>Где user_id необходимо указать id пользователя</p>
