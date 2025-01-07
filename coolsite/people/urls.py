from django.urls import path, re_path
from people.views import pageNotFound

from .views import * 

urlpatterns = [
    path('', PeopleHome.as_view(), name='home'),  # Главная страница
    path('about/', about, name='about'),  # Страница "О сайте"
    path('addpage/', AddPage.as_view(), name='add_page'),  # Добавление статьи
    path('contact/', contact, name='contact'),  # Обратная связь
    path('login/', login, name='login'),  # Авторизация
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'), #Посты
    path('category/<slug:cat_slug>/', PeopleCategory.as_view(), name='category'), # Маршрут для отображения постов определённой категории
]





