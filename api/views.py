from django.utils import timezone
from rest_framework import generics
from rest_framework.response import Response
from ques.models import Poll, UserPoll
from api.serializers import PollSerializer, PollQuestionSerializer, AnswerPollSerializer, UserAnswerSerializer
from rest_framework.views import APIView


class PollListView(generics.ListAPIView):
    """Список активных опросов"""
    serializer_class = PollSerializer

    def get_queryset(self):
        actual_date = timezone.now()
        polls = Poll.objects.filter(start_date__lte=actual_date, end_date__gte=actual_date)
        return polls


class TakePollView(generics.ListAPIView):
    """Список опроса с встроенными вопросами и вариантами ответов"""
    serializer_class = PollQuestionSerializer

    def get_queryset(self):
        pk_poll = self.kwargs['pk']
        actual_date = timezone.now()
        take_poll = Poll.objects.filter(start_date__lte=actual_date, end_date__gte=actual_date, pk=pk_poll)
        return take_poll


class AnswerPollCreateViews(APIView):
    """Сохранение полученных результатов опроса"""

    def post(self, request):
        answer = AnswerPollSerializer(data=request.data)
        if answer.is_valid():
            answer.save()
        return Response(status=201)


class AnswerUserList(generics.ListAPIView):
    """Пройденный опрос"""
    serializer_class = UserAnswerSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        answer = UserPoll.objects.filter(user_id__user_id=user_id)
        return answer
