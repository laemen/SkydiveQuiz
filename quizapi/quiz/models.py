from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    question = models.TextField()
    image = models.ImageField(blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ('{} - {}'.format(self.id, self.title))
    

class Answer(models.Model):
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 related_name="answers")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.TextField()
    correct = models.BooleanField(default=False)
    image = models.ImageField(blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ('{} - {}'.format(self.id, self.answer))
    

class Profile(models.Model):

    SKYDIVE_LICENSES_CHOICES = (
        ('AFF', 'AFF'),
        ('AO', 'AO'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skydive_license = models.CharField(max_length=20,
                                       choices=SKYDIVE_LICENSES_CHOICES)

    def __str__(self):
        return '[{}] - {} {}'.format(self.user.username, 
                                     self.user.first_name, 
                                     self.user.last_name)
