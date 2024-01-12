from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    topic_name = models.CharField(max_length=234, unique=True)

    def __str__(self):
        return self.topic_name


class webPage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    url = models.URLField()

    def __str__(self):
        return self.name


class accessRecord(models.Model):
    webpage_recd = models.ForeignKey(webPage, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    email = models.EmailField()

    def __str__(self):
        return self.name


class user_profileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)
    portfolio_url = models.URLField(blank=True)

    def __str__(self):
        return self.user.username



