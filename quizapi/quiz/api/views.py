from rest_framework import generics

from quiz.models import Question, Answer
from quiz.api.serializers import QuestionSerializer, AnswerSerializer


class QuestionListCreateAPIView(generics.ListCreateAPIView):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer




class AnswerListCreateAPIView(generics.ListCreateAPIView):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
