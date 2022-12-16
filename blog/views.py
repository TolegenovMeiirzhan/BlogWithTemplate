from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import *
from .models import *
# Create your views here.

class HomePost(ListView):
    model = Posts
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'All Posts'
        context['popular'] = Posts.objects.order_by('-views')[:1]
        return context

    # def get_queryset(self):
        # return

class ViewPost(DetailView):
    model = Posts
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Posts.objects.get(slug=self.kwargs['slug'])
        self.object.views = F('views')+1
        self.object.save()
        self.object.refresh_from_db()
        return context


class Get_category(ListView):
    model = Category
    template_name = 'blog/category.html'
    context_object_name = 'posts'
    allow_empty = False
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context

    def get_queryset(self):
        return Posts.objects.filter(category__slug=self.kwargs['slug'])

class Get_tags(ListView):
    model = Tag
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Posts by tag ' + str(Tag.objects.get(slug=self.kwargs['slug']))
        return context

    def get_queryset(self):
        return Posts.objects.filter(tags__slug=self.kwargs['slug'])

class Search(ListView):
    model = Posts
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Posts.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['s'] = F"s={self.request.GET.get('s')}&"
        return context
