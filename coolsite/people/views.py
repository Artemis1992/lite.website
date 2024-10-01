from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render

def index(request):
    return HttpResponse("Страница приложения people")


def categories(request, catid):
    if(request.GET):
        print(request.GET)  # Выводим параметры в терминал
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2024:
        return redirect('home', permanent=True) # Редирект
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


