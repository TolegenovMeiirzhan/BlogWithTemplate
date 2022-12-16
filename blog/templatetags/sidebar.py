from django import template

from blog.models import Posts, Tag

register = template.Library()

@register.inclusion_tag('blog/list_sidebar.html')
def get_sidebar(cnt=3):
    posts = Posts.objects.order_by('-views')[:cnt]
    return {'posts': posts}

@register.inclusion_tag('blog/list_tags.html')
def get_tags():
    tags = Tag.objects.all()
    return {'tags': tags}