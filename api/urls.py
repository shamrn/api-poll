from django.urls import path
from . import views



urlpatterns = [
    path('poll-list/',views.PollListView.as_view()),
    path('take-poll/<pk>/',views.TakePollView.as_view()),
    path('create-answer/',views.AnswerPollCreateViews.as_view()),
    path('list-answer/<user_id>/',views.AnswerUserList.as_view()),
]
