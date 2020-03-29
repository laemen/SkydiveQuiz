from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from quiz.models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = "__all__"



class QuestionSerializer(serializers.ModelSerializer):

    answers = AnswerSerializer(many=True, read_only=True)
    time_since_publication = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = "__all__"

    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta



