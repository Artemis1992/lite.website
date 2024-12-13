from django import template
from people.models import *
from people.views import menu # из views.py
from people.views import show_category, index

register = template.Library()



@register.simple_tag(name="getcats") # Регистрация простого тега для получения категорий
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag("people/list_categories.html")
def show_categories(sort=None, cat_selected=0):
    """
    Включающий тег для отображения списка категорий и меню.
    
    :param sort: Параметр для сортировки категорий.
    :param cat_selected: ID выбранной категории.
    :return: Словарь с данными для рендеринга шаблона.
    """
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
        
    return {
        "cats": cats, 
        "cat_selected": cat_selected,
    }


@register.inclusion_tag("people/list_menu.html")
def show_menu():
        return {
            "menu": menu,
        }







