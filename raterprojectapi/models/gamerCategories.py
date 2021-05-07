from raterprojectapi.models.games import Game
from raterprojectapi.models.categories import Category
from django.db import models

class GamerCategory(models.Model):
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)