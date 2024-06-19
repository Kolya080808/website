from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return HttpResponse("<a href='https://www.youtube.com/watch?v=j-iheFkstFQ'>Отличная штука, этот текст. Нажми на меня.</a>")