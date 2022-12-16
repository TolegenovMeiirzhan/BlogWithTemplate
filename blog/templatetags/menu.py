from django import template
from blog.models import Category

register = template.Library()

@register.inclusion_tag('blog/list_menu.html')
def show_menu(m_class='menu'):
    categories = Category.objects.all()
    return {'categories': categories, 'm_class': m_class}