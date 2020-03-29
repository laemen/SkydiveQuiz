from django.urls import path
from quiz.api.views import (QuestionListCreateAPIView, QuestionDetailAPIView,
                            AnswerListCreateAPIView, AnswerDetailAPIView)


urlpatterns = [
    path("questions/", 
         QuestionListCreateAPIView.as_view(), 
         name="question-list"),

    path("questions/<int:pk>", 
         QuestionDetailAPIView.as_view(), 
         name="question-detail"),

    path("answers/", 
         AnswerListCreateAPIView.as_view(), 
         name="answer-list"),

    path("answers/<int:pk>", 
         AnswerDetailAPIView.as_view(), 
         name="answer-detail")]