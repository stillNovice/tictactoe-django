from django.http import HttpResponse

def welcome(request):
  return HttpResponse('hello from this side')