from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *
# Register your models here.

class PostsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Posts
        fields = '__all__'


class PostsAdmin(admin.ModelAdmin):
    form = PostsAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'updated_at', 'author', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'author')
    # list_editable = ('title',)
    list_filter = ('created_at', 'updated_at', 'category', 'tags')
    fields = ('id', 'title', 'slug', 'content', 'author', 'get_photo', 'photo', 'category', 'tags', 'created_at', 'updated_at', 'views')
    readonly_fields = ('id', 'created_at', 'updated_at', 'views', 'get_photo')
    save_on_top = True
    save_as = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src={ obj.photo.url } width='75'>")

    get_photo.short_description = 'image'

admin.site.register(Posts, PostsAdmin)

class Categoryadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title', 'slug')
    search_fields = ('id', 'title')
admin.site.register(Category, Categoryadmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title', 'slug')
    search_fields = ('id', 'title')

admin.site.register(Tag, TagAdmin)