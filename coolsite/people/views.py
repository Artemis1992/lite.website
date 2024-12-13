# HttpResponse: возвращает простой HTTP-ответ с текстом, который может быть строкой HTML.
# render: рендерит HTML-шаблон с возможностью передавать контекстные данные в шаблон для более сложной логики отображения.
# redirect: выполняет перенаправление на другой URL. Можно использовать параметр permanent для указания, является ли перенаправление временным (302) или постоянным (301).
# HttpResponseNotFound: возвращает ошибку 404 с указанным HTML-сообщением.

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import get_object_or_404, redirect, render

from .models import *

menu = [{"title": "О сайте", "url_name": "about"},
        {"title": "Добавить статью", "url_name": "add_page"},
        {"title": "Обратная связь", "url_name": "contact"},
        {"title": "Войти", "url_name": "login"},
]



def index(request):
    """
    Эта функция обрабатывает запрос для главной страницы приложения.
    Она выбирает все записи из модели People и все категории из модели Category.
    Контекст, содержащий список записей, категории, меню, заголовок страницы и выделенную категорию (0 — для всех категорий),
    передаётся в шаблон 'people/index.html' для отображения содержимого главной страницы.
    """
    posts = People.objects.all()
    
    context = {
        'posts': posts,        # Список записей
        'title': 'Главная страница',  # Заголовок страницы
        'cat_selected': 0,     # Выбранная категория (0 — все категории)
    }

    return render(request, 'people/index.html', context=context)



def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")



def show_category(request, cat_id):
    """
    Эта функция обрабатывает запрос для отображения записей, относящихся к определённой категории (cat_id).
    Она выбирает записи модели People, у которых поле cat_id совпадает с переданным параметром.
    Если записи не найдены, вызывается исключение Http404.
    Контекст с данными (записи, категории, меню, заголовок и выделенная категория) передаётся в шаблон 'people/index.html' для рендеринга.
    """
    posts = People.objects.filter(cat_id=cat_id) 

    
    if len(posts) == 0:
        raise Http404
    
    context = {
        'posts': posts,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, 'people/index.html', context=context)
     
     
     
def about(request):
    return render(request, 'people/about.html', {"menu": menu, 'title': 'О сайте'})

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная сязь")

def login(request):
    return HttpResponse("Авторизация")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


