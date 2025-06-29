from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'caption', 'created_at')
    search_fields = ('author__username', 'caption')
    list_filter = ('created_at',)
