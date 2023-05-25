from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()


class Club(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Member, related_name="clubs")


class Post(models.Model):
    text = models.TextField
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="posts")
