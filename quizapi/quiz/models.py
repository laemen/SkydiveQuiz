from django.db import models

class Question(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=120)
    question = models.TextField()
    image = models.ImageField(blank=True, null=True)
    publication_date = models.DateField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ('{} - {}'.format(self.id, self.title))
    

class Answer(models.Model):
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 related_name="answers")
    author = models.CharField(max_length=50)
    answer = models.TextField()
    correct = models.BooleanField(default=False)
    image = models.ImageField(blank=True, null=True)
    publication_date = models.DateField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ('{} - {}'.format(self.id, self.answer))
    