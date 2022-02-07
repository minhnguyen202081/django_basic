from django.db import models
from django.conf import settings
from django.utils import timezone


class Tag(models.Model):
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag


class Memory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='memories')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,models.CASCADE)
    posted_on = models.DateField(default=timezone.now)
    date = models.DateField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
