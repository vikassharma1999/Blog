from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Articles(models.Model):
    title=models.CharField(max_length=20)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    thumb=models.ImageField(default='default.jpg',blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.title
    def snippat(self):
        return self.body[:50]+"..."
