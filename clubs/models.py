from django.db import models


class People(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()


class Club(models.Model):
    name = models.CharField(max_length=100)
    poeples = models.ManyToManyField(People, related_name="clubs")


class Post(models.Model):
    text = models.TextField
    people = models.ForeignKey(People, on_delete=models.CASCADE, related_name="posts")
