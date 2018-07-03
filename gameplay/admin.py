from django.contrib import admin

from .models import Game, Move

# ModelAdmin class
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
  list_display = ('id', 'first_player', 'second_player', 'game_status')
  list_editable = ['game_status']

# Register your models here.
admin.site.register(Move)
