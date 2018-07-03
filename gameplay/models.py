from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User

GAME_STATUS_CHOICES = (
  ('F', 'First Player To Move'),
  ('S', 'Second Player To Move'),
  ('W', 'First Player Wins'),
  ('L', 'Second Player Wins'),
  ('D', 'Draw')
)

# Define custom operations on a QuerySet
class GameQuerySet(models.QuerySet):
  def games_for_user(self, user):
    return self.filter(
      Q(first_player = user) | Q(second_player = user)  
    )
  
  def active_games(self):
    return self.filter(
      Q(game_status = 'F') | Q(game_status = 'S')
    )

class Game(models.Model):
  first_player = models.ForeignKey(User,  verbose_name="PLAYER ONE", related_name='game_first_player', on_delete=models.CASCADE)
  second_player = models.ForeignKey(User, verbose_name="PLAYER TWO", related_name='game_second_player', on_delete=models.CASCADE)
  start_time = models.DateTimeField(auto_now_add=True)
  last_active = models.DateTimeField(auto_now=True)
  game_status = models.CharField(max_length=1, default='F', choices=GAME_STATUS_CHOICES)

  # overriding the manager object for our Model class, to make the custom operations available for use
  objects = GameQuerySet.as_manager()

  def __str__(self):
    return "{0} vs {1}".format(self.first_player, self.second_player)

class Move(models.Model):
  x = models.IntegerField()
  y = models.IntegerField()
  comments = models.CharField(max_length=300, blank=True)
  move_by_first_player = models.BooleanField()
  game = models.ForeignKey(Game, on_delete=models.CASCADE)