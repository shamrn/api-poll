from rest_framework import serializers
from ques.models import Poll, Question, QuesChoices, UserAnswerQues, UserId, UserPoll


class PollSerializer(serializers.ModelSerializer):
    """Сериализация опросов"""

    class Meta:
        model = Poll
        fields = '__all__'


class QuesChoicesSerializer(serializers.ModelSerializer):
    """Сериализация выбора ответа"""

    class Meta:
        model = QuesChoices
        fields = ('id', 'desc')


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализация вопросов"""
    ques_choices = QuesChoicesSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'desc', 'type', 'ques_choices')


class PollQuestionSerializer(serializers.ModelSerializer):
    """Сериализация опроса с встроенными вопросами и вариантами ответов"""
    question = QuestionSerializer(many=True)

    class Meta:
        model = Poll
        fields = ('id', 'name', 'desc', 'question')


class AnswerPollSerializer(serializers.Serializer):
    """Сериализция ответов на опрос"""
    user_id = serializers.IntegerField()  # Ожидаем принять id - пользователя
    poll = serializers.IntegerField()  # Ожидаем принять id - опроса
    question = serializers.JSONField()  # Ожидаем принять словарь, в виде id - вопроса : id - ответа/ответов/текста

    def create(self, request):
        user_id = request.pop('user_id')

        if not UserId.objects.filter(user_id=user_id).exists():  # Если пользователя нет в базе
            user = UserId.objects.create(user_id=user_id)  # создаем его в базе
        else:
            user = UserId.objects.get(user_id=user_id)

        poll = Poll.objects.get(pk=request.pop('poll'))

        user_poll = UserPoll.objects.create(user_id=user,
                                            poll=poll)  # создаем поле с пользователем и опросом который он проходит

        question = request.pop('question')
        # Проходимся по каждому вопросу и его ответу/ответов, создаем под каждый ответ отдельное
        # поле в БД, где поля user_poll - fk опрос который прошел пользователь, question - fk вопрос,
        # text - свой вариант ответа , ques_choices - m2m к полю или полям вариантов ответа
        for que in question:
            user_answer = UserAnswerQues(user_poll=user_poll)
            for key, value in que.items():
                question = Question.objects.get(pk=key)
                user_answer.question = question

                if not ''.join(value).isdigit():
                    user_answer.text = ''.join(value)
                    user_answer.save()
                else:
                    user_answer.save()
                    user_answer.ques_choices.set(value)
        return user_answer



class UserAnswerQuesSerializer(serializers.ModelSerializer):
    question = serializers.SlugRelatedField(slug_field='desc',read_only=True)
    ques_choices = serializers.SlugRelatedField(slug_field='desc',read_only=True,many=True)

    class Meta:
        model = UserAnswerQues
        fields = ('text', 'question', 'ques_choices')

class UserAnswerSerializer(serializers.ModelSerializer):
    """Сериализция пользователя и пройденного опроса, включает в себя вопросы и ответы"""
    user_id = serializers.SlugRelatedField(slug_field='user_id',read_only=True)
    poll = serializers.SlugRelatedField(slug_field='name',read_only=True)
    user_poll = UserAnswerQuesSerializer(many=True)

    class Meta:
        model = UserPoll
        fields = ('user_id','poll','user_poll')

