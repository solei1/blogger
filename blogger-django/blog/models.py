from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField('标题', max_length=60)
    pub_date = models.DateTimeField('发布日期', default=timezone.now())
    body = models.TextField('正文')
    view_count = models.PositiveIntegerField('浏览数', default=0)
    tags = models.ManyToManyField('Tag', verbose_name='标签', blank=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField('', max_length=20)

    def __str__(self):
        return  self.name

class Link(models.Model):
    category = models.CharField('类别', max_length=10)
    link = models.CharField('链接', max_length=50)
    intro = models.CharField('简介', max_length=50)
    create_time = models.DateTimeField('创建时间', default=timezone.now())

    def __str__(self):
        return  self.intro
# Create your models here.
