from raterprojectapi.models.players import Player
from django.db import models

class Review (models.Model):

    title = models.CharField(max_length=50)
    review = models.CharField(max_length=50)
    rating = models.IntegerField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE)