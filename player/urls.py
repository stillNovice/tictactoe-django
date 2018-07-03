from django.urls import path

#from player.views import home
from player import views

urlpatterns = [
    path('home', views.home, name="Player"),
]