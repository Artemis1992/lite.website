from django.urls import path, re_path
from people.views import pageNotFound

from .views import * 

urlpatterns = [
    path('', index, name='home'),  # Главная страница
    path('about/', about, name='about'),  # Страница "О сайте"
    path('addpage/', addpage, name='add_page'),  # Добавление статьи
    path('contact/', contact, name='contact'),  # Обратная связь
    path('login/', login, name='login'),  # Авторизация
    path('post/<int:post_id>/', show_post, name='post'), #Посты
    path('category/<int:cat_id>/', show_category, name='category'), # Маршрут для отображения постов определённой категории
]





