from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.decorators import login_required # Декоратор для ограничения доступа к авторизованным пользователям
from django.core.paginator import Paginator

from .forms import *
from .models import *
from .utils import *



class PeopleHome(DataMixin, ListView):
    model = People
    template_name = "people/index.html" # Вместо создание нового шаблона указываем старый.
    context_object_name = "posts" # Для того чтобы оставить posts в шаблолне index.html, явно указываем ее. 

    # Формирование контекста
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) # Получаем базовый контекст от родительского класса
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return People.objects.filter(is_published=True)
    
    
    
# # Главная страница, отображает все записи
# def index(request):
#     posts = People.objects.all()  # Получаем все записи из модели People
#     context = {
#         'posts': posts,        # Список записей
#         'title': 'Главная страница',  # Заголовок страницы
#         'cat_selected': 0,     # Выбранная категория (0 — все категории)
#     }
#     return render(request, 'people/index.html', context=context)


class ShowPost(DataMixin, DetailView):
    model = People
    template_name = "people/post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = 'post'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return {**context, **c_def} 

    

# Отображение конкретного поста
# def show_post(request, post_slug):
#     post = get_object_or_404(People, slug=post_slug)  # Получаем пост или вызываем 404, если не найден

#     context = {
#         'post': post,
#         'title': post.title,
#         'cat_selected': post.cat_id,  # Идентификатор выбранной категории
#     }
    
#     return render(request, 'people/post.html', context=context)



class PeopleCategory(DataMixin, ListView):
    model = People
    template_name = 'people/index.html'
    context_object_name = 'posts'
    # allow_empty = False
    
    def get_queryset(self):
        return People.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context =  super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Категория - " + str(context["posts"][0].cat),
                                      cat_selected=context["posts"][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))
        # if isinstance(c_def, dict):
        #     return {**context, **c_def}
        # else:
        #     return context
    




# # Отображение постов по категории
# def show_category(request, cat_id):
#     posts = People.objects.filter(cat_id=cat_id)  # Получаем посты по категории

#     if len(posts) == 0:
#         raise Http404  # Если посты не найдены, генерируем ошибку 404
    
#     context = {
#         'posts': posts,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat_id,
#     }
#     return render(request, 'people/index.html', context=context)
 
 
 
 
    
# Страница "О сайте"
# @login_required  # Декоратор, обеспечивающий доступ к функции только для авторизованных пользователей
def about(request):
    contact_list = People.objects.all()
    paginator = Paginator(contact_list, 3)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'people/about.html', {'page_obj': page_obj, "menu": menu, 'title': 'О сайте'})




class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = "people/addpage.html"
    # seccess_url = reverse_lazy("home")
    login_url = "/register/"   # Временно выставили для того чтобы через админ панель можно было добавлять посты.
    # login_url = reverse_lazy("home")
    # raise_exception = True  # Формирует страницу 403 доступ запрещен.
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        return dict(list(context.items()) + list(c_def.items()))


# # Страница для добавления статьи
# def addpage(request):
#     # Если запрос был отправлен методом POST (пользователь отправил форму)
#     if request.method == "POST":
#         form = AddPostForm(request.POST, request.FILES) # Форма с заполненными данными
#         if form.is_valid(): # Проверяем, валидны ли данные, введённые пользователем
#             # Перенаправляем пользователя на главную страницу после успешного добавления
#             form.save()
#             return redirect("home")
#     else:# Если пользователь просто открыл страницу
#         form = AddPostForm() # Создаём пустую форму
#     # Возвращаем шаблон `addpage.html`, передавая форму, меню и заголовок страницы
#     return render(request, 'people/addpage.html', {
#         'form': form, 
#         'menu': menu, 
#         'title': "Добавление статьи"
#     })



# Страница обратной связи
def contact(request):
    return render(request, 'people/contact.html', {'menu': menu, 'title': "Обратная сязь"})

# Страница для авторизации    
def login(request):
    return render(request, 'people/login.html', {"menu": menu, "title": "Авторизация"})

# Обработчик страницы 404
def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")  # Возвращаем ошибку 404 с сообщением

# Страница для регистрации 
class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm # Используем класс формы из файла forms.py
    template_name = 'people/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))



