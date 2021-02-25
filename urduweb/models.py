from django.db import models
from datetime import date
from django.urls import reverse
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="Images/")
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    description = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    post_view = models.IntegerField(default=0)
    video_url = models.URLField(null=True, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=255)
    message = models.TextField()
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
