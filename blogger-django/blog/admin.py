from django.contrib import admin
from .models import Article, Tag, Link

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'view_count')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
admin.site.register(Link)
# Register your models here.
