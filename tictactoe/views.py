from django.shortcuts import render

def welcome(request):
  return render(request, "tictactoe/home.html", {})