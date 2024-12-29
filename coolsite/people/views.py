from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import get_object_or_404, redirect, render

from .forms import *
from .models import *

menu = [{"title": "О сайте", "url_name": "about"},
        {"title": "Добавить статью", "url_name": "add_page"},
        {"title": "Обратная связь", "url_name": "contact"},
        {"title": "Войти", "url_name": "login"},
]


# Главная страница, отображает все записи
def index(request):
    posts = People.objects.all()  # Получаем все записи из модели People

    context = {
        'posts': posts,        # Список записей
        'title': 'Главная страница',  # Заголовок страницы
        'cat_selected': 0,     # Выбранная категория (0 — все категории)
    }

    return render(request, 'people/index.html', context=context)



# Отображение конкретного поста
def show_post(request, post_slug):
    post = get_object_or_404(People, slug=post_slug)  # Получаем пост или вызываем 404, если не найден

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,  # Идентификатор выбранной категории
    }
    
    return render(request, 'people/post.html', context=context)



# Отображение постов по категории
def show_category(request, cat_id):
    posts = People.objects.filter(cat_id=cat_id)  # Получаем посты по категории

    if len(posts) == 0:
        raise Http404  # Если посты не найдены, генерируем ошибку 404
    
    context = {
        'posts': posts,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, 'people/index.html', context=context)
 
 
    
# Страница "О сайте"
def about(request):
    return render(request, 'people/about.html', {"menu": menu, 'title': 'О сайте'})


# Страница для добавления статьи
def addpage(request):
    if request.method == "POST":
        form = AddPostForm(request.POST) # Форма с заполненными данными
        if form.is_valid(): # Проверка корректности данных
            # print(form.cleaned_data) # Вывод очищенных данных в консоль
            try:
                People.objects.create(**form.cleaned_data)
                return redirect("home")
            except:
                form.add_error(None, "Ошибка добавление поста")
        else:
            form =AddPostForm() # Пустая форма, если данные некорректны
    else:
        form = AddPostForm() # Пустая форма для первого отображения
    
    return render(request, 'people/addpage.html', {'form': form, 'menu': menu, 'title': "Добавление статьи"})



# Страница обратной связи
def contact(request):
    return render(request, 'people/contact.html', {'menu': menu, 'title': "Обратная сязь"})

# Страница для авторизации
def login(request):
    return render(request, 'people/login.html', {"menu": menu, "title": "Авторизация"})

# Обработчик страницы 404
def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")  # Возвращаем ошибку 404 с сообщением
