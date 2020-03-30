from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework import status
from rest_framework.generics import (GenericAPIView, get_object_or_404, 
                                     ListCreateAPIView, 
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from quiz.models import Answer, Profile, Question
from quiz.api.permissions import IsAdminUser, IsAuthorOrReadOnly
from quiz.api.serializers import (AnswerSerializer, ProfileSerializer, 
                                  QuestionSerializer)


class QuestionListCreateAPIView(ListCreateAPIView):

    queryset = Question.objects.all().order_by('id')
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthorOrReadOnly]


class QuestionDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Question.objects.all().order_by('id')
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)


class AnswerListCreateAPIView(ListCreateAPIView):

    queryset = Answer.objects.all().order_by('id')
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthorOrReadOnly]


class AnswerDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Answer.objects.all().order_by('id')
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)



class ProfileListCreateAPIView(ListCreateAPIView):

    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]


class ProfileDetailAPIView2(RetrieveUpdateDestroyAPIView):

    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)



class ProfileDetailAPIView(APIView):

    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]

    def get_object(self, pk):
        profile = get_object_or_404(Profile, pk=pk)
        return profile

    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

