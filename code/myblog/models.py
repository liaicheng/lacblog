#coding=utf-8
from django.db import models


class Tag(models.Model):
    tag_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tag_name


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    tag = models.ManyToManyField(Tag, blank=True)
    summary = models.TextField()
    timestamp = models.DateTimeField()

    def __unicode__(self):
        return u'%s %s %s' % (self.title, self.author, self.timestamp)

    class Meta(object):
        ordering = ['-timestamp']

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('blog.views.blog_show', args=[str(self.id)])

# 下面的Paragraph、Photo、Code类代表着博客正文中的文字段落、代码以及图片
# 它们各有一个sequence属性，用来表示这些models在博客正文中所出现的顺序。

class Paragraph(models.Model):
    discern = "paragraph"
    describe = models.CharField(max_length=100)
    sequence = models.PositiveSmallIntegerField()
    tag = models.ManyToManyField(BlogPost)
    paragraph = models.TextField()

    def __unicode__(self):
        return self.describe


class Photo(models.Model):
    discern = "photo"
    sequence = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=100)
    #image = models.ImageField(upload_to='photos', blank=True)
    tag = models.ManyToManyField(BlogPost)
    url = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title


class Code(models.Model):
    discern = "code"
    sequence = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=150)
    content = models.TextField()
    tag = models.ManyToManyField(BlogPost)

    def __unicode__(self):
        return self.title
