from django import template
from people.models import *
from people.views import menu, show_post

register = template.Library()



@register.simple_tag(name="getcats") # мы изменили имя с get_categories на getcats.
def get_categories():
    return Category.objects.all()



@register.inclusion_tag('people/list_categories.html')
def show_categories():
    cats = Category.objects.all()
    return {'cats': cats}


@register.inclusion_tag('people/list_menu.html')
def show_menu():
    return {
        'menu': menu,
    }

