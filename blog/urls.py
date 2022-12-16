from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePost.as_view(), name='home'),
    path('category/<str:slug>/', Get_category.as_view(), name='category'),
    path('post/<str:slug>/', ViewPost.as_view(), name='post'),
    path('tag/<str:slug>/', Get_tags.as_view(), name='tag'),
    path('search/', Search.as_view(), name='search'),

]