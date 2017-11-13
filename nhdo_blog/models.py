from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    title = models.CharField(max_length=40)
    content = models.TextField(max_length=10000)
    date = models.DateTimeField(auto_now=True, blank=True, null=True)
    pic = models.FileField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']


class Comment(models.Model):
    user = models.ForeignKey(User, blank=True,null=True)
    box = models.ForeignKey(Blog, blank=True,null=True)
    comment = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.user)
