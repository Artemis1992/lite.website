from django import template
from people.models import *  # Импортируем все модели из people приложения
from people.views import menu  # Импортируем переменную menu из views


register = template.Library()  # Создаем экземпляр библиотеки шаблонов


# Определение тега шаблона getcats, который возвращает все категории
@register.simple_tag(name="getcats")  # Задаем имя тега "getcats"
def get_categories():
    return Category.objects.all()  # Возвращаем все объекты категории


# Определение тега шаблона show_categories, который рендерит список категорий
@register.inclusion_tag('people/list_categories.html')  # Шаблон для отображения категорий
def show_categories():
    cats = Category.objects.all()  # Получаем все категории
    return {'cats': cats}  # Передаем категории в шаблон


# Определение тега шаблона show_menu, который рендерит меню
@register.inclusion_tag('people/list_menu.html')  # Шаблон для отображения меню
def show_menu():
    return {
        'menu': menu,  # Передаем переменную menu в шаблон
    }
