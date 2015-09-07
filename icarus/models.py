from django.db import models
from datetime import datetime;

class highScore(models.Model):
	score = models.IntegerField(default=0)
	user = models.CharField(max_length=50)
	creationDate = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return "score: " + str(self.score) + "  user: " + str(self.user)
