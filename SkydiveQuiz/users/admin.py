from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import SkydiveQuizUser

class SkydiveQuizUserAdmin(UserAdmin):
    # add_form =
    # form =
    model = SkydiveQuizUser
    list_display = ["username", "email", "is_staff"]

admin.site.register(SkydiveQuizUser, SkydiveQuizUserAdmin)