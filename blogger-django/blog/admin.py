from django.contrib import admin
from .models import Article, Tag

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'view_count')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
# Register your models here.
