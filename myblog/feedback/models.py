from django.db import models

# Create your models here.
class FeedBack(models.Model):
	feed_back=models.CharField(max_length=200)

	def __str__(self):
		return self.feed_back
