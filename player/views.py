from django.shortcuts import render
from django.http import HttpResponse

from gameplay.models import Game

def home(request):
  """
  games_first_player = Game.objects.filter(
    first_player = request.user,
    game_status = 'F'
  )

  games_second_player = Game.objects.filter(
    second_player = request.user,
    game_status = 'S'
  )

  context = {
    'all_games': list(games_first_player) + list(games_second_player)
  }
  """

  # using Querysets and custom managers
  my_games = Game.objects.games_for_user(request.user)
  active_games = my_games.active_games()

  context = {
    'active_games': active_games 
  }
  
  # django searches templates in the templates folder automatically, so the path of the template is relative to "templates" folder
  return render(request, "player/home.html", context)