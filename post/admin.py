from django import forms
from django.contrib import admin
from .models import Post, Like, Bookmark, Comment, Tag

class LikeInline(admin.TabularInline): # 어드민 페이지 정리
    model=Like

    
class CommentInline(admin.TabularInline):
    model = Comment

    
class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Post
        fields = '__all__'

        
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'nickname', 'content', 'created_at']
    list_display_links = ['author', 'nickname', 'content']
    form = PostForm
    inlines = [LikeInline, CommentInline]
    
    def nickname(request, post):
        return post.author.profile.nickname
    

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'created_at'] # 보여주는 부분
    list_display_links = ['post', 'user'] # 링크가 달리는 부분


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'created_at']
    list_display_links = ['post', 'user']

    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'content', 'author', 'created_at']
    list_display_links = ['post', 'content', 'author']
    
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']