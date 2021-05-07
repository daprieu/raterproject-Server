from django.db.models.deletion import SET_NULL
from raterprojectapi.models.reviews import Review
from raterprojectapi.models.players import Player
from django.db import models

class Game(models.Model):

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    designer = models.CharField(max_length=50)
    year_released = models.IntegerField()
    num_players = models.IntegerField()
    play_time = models.IntegerField()
    age = models.IntegerField()
    player = models.ForeignKey(Player, on_delete=SET_NULL, null=True)
    review = models.ForeignKey(Review, on_delete=SET_NULL, null=True)