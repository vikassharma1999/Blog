from django.db import models

# Create your models here.
class FeedBack(models.Model):
	feed_back=models.CharField(max_length=200)

	def __str__(self):
		return self.feed_back

class Text(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField()
	mob_no=models.CharField(max_length=10)
	query=models.TextField()

	def __str__(self):
		return self.name