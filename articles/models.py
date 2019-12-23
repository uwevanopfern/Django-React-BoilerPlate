from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=120)
    owner = models.CharField(max_length=50, default='Dude')
    content = models.TextField()

    def __str__(self):
        return self.title
