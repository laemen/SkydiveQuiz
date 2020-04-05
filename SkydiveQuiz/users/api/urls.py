from django.urls import path
from users.api.views import SkydiveQuizUserAPIView

urlpatterns = [
    path("user/", SkydiveQuizUserAPIView.as_view(), name="skydivequiz-user")
]