# HttpResponse: возвращает простой HTTP-ответ с текстом, который может быть строкой HTML.
# render: рендерит HTML-шаблон с возможностью передавать контекстные данные в шаблон для более сложной логики отображения.
# redirect: выполняет перенаправление на другой URL. Можно использовать параметр permanent для указания, является ли перенаправление временным (302) или постоянным (301).
# HttpResponseNotFound: возвращает ошибку 404 с указанным HTML-сообщением.

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render

from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    posts = People.objects.all()
    return render(request, 'people/index.html', {"posts": posts, "menu": menu, 'title': 'Главная сттроаница'})

def about(request):
    return render(request, 'people/about.html', {"menu": menu, 'title': 'О сайте'})

def categories(request, catid):
    if(request.GET):
        print(request.GET)  # Выводим параметры в терминал
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")

def archive(request, year):
    # Если год больше 2024, выполняем редирект на главную страницу
    if int(year) > 2024:
        return redirect('home', permanent=True) # Редирект
    # Возвращаем HttpResponse с заголовком и значением года
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


