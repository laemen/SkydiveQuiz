from django.urls import path
from users.api.views import CustomUserAPIView

urlpatterns = [
    path("user/", CustomUserAPIView.as_view(), name="custom-user")
]