from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers

from quiz.models import Answer, Profile, Question


class AnswerSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Answer
        fields = "__all__"



class QuestionSerializer(serializers.ModelSerializer):

    answers = AnswerSerializer(many=True, read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    time_since_publication = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = "__all__"

    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        time_delta = None
        if publication_date is not None:
            now = datetime.now()
            time_delta = timesince(publication_date, now)
        return time_delta



class ProfileSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"

