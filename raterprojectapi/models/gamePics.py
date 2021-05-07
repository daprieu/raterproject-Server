from raterprojectapi.models.players import Player
from django.db.models.deletion import SET_NULL
from raterprojectapi.models.games import Game
from django.db import models

class GamePic(models.Model):

    image_url = models.ImageField(upload_to ='uploads/')
    game = models.ForeignKey(Game, on_delete=SET_NULL, null=True)
    player = models.ForeignKey(Player, on_delete=SET_NULL, null=True)