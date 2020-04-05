from django.db import models
from django.contrib.auth.models import AbstractUser

class SkydiveQuizUser(AbstractUser):

    """
    SKYDIVE_LICENSES_CHOICES = (
        ('AFF', 'AFF'),
        ('AO', 'AO'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),)

    skydive_license = models.CharField(max_length=20,
                                       choices=SKYDIVE_LICENSES_CHOICES)
    skydive_license_country = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    """

    def __str__(self):
        return ('{} {} [{}]'.format(self.first_name, self.last_name, 'C'))
