from django_registration.forms import RegistrationForm
from users.models import SkydiveQuizUser


class SkydiveQuizUserForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = SkydiveQuizUser