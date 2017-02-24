from django.db import models


class Article(models.Model):
    title = models.CharField('标题', max_length=60)
    pub_date = models.DateTimeField('发布日期')
    body = models.TextField('正文')
    view_count = models.PositiveIntegerField('浏览数', default=0)
    tags = models.ManyToManyField('Tag', verbose_name='标签', blank=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField('', max_length=20)

    def __str__(self):
        return  self.name


# Create your models here.
