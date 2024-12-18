from django import template
from people.models import *
from people.views import menu, show_post

register = template.Library()



@register.simple_tag(name="getcats") # мы изменили имя с get_categories на getcats.
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)



@register.inclusion_tag('people/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    
    return {"cats": cats, "cat_selected": cat_selected}


@register.inclusion_tag('people/list_menu.html')
def show_menu():
    return {
        'menu': menu,
    }

