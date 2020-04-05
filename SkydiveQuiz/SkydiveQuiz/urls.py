"""SkydiveQuiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

from django_registration.backends.one_step.views import RegistrationView

from core.views import IndexTemplateView
from users.forms import SkydiveQuizUserForm

# http://django-registration.readthedocs.io/en/3.0/activation-workflow.html

urlpatterns = [
    # admin url
    path('admin/', admin.site.urls),

    # custome registration view for SkydiveQuiz user
    path('accounts/register/', 
        RegistrationView.as_view(
            form_class=SkydiveQuizUserForm,
            success_url="/",
    ), name="django_registration_register"),

    # other urls used by the django_registration package
    path('accounts/', 
        include("django_registration.backends.one_step.urls")),

    # login urls provided by django to login users via the browser
    path('accounts/', 
        include("django.contrib.auth.urls")),

    # url file at users/api/urls.py
    path('api/', 
        include("users.api.urls")),

    # login url for the browsable api
    path('api-auth/', 
        include("rest_framework.urls")),

    # login endpoints to use via REST
    path('api/rest-auth/', 
        include("rest_auth.urls")),

    # registration endpoint to use via REST
    path('api/rest-auth/registration', 
        include("rest_auth.registration.urls")),
        
    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point")
]
