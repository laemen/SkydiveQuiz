from rest_framework import serializers
from users.models import SkydiveQuizUser

class UserDisplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = SkydiveQuizUser
        fields = ["username"]