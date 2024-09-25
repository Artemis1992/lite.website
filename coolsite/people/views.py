from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Страница приложения people")

def categories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")

# def artist(request):
#     return HttpResponse("<h2>Актрисы</h2>")




