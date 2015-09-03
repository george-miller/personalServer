from django.db import models

# Create your models here.
class highScore(models.Model):
	score = models.IntegerField(default=0)
	user = models.CharField(max_length=50)

	def __str__(self):
		return "score: " + score + "  user: " + user
