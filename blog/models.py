# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
    """docstring for Category"""
    category_name = models.CharField(max_length=20, verbose_name=u'类名')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')

    def __unicode__(self):
        return self.category_name

class SubCategory(models.Model):
    category_name = models.CharField(max_length=20,verbose_name=u'子类')
    category = models.ForeignKey(Category,blank=True,verbose_name=u'主类')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间')

    def __unicode__(self):
        return self.category_name


class Author(models.Model):
    """docstring for Author"""
    name = models.CharField(max_length=30, verbose_name=u'作者名')
    email = models.EmailField(blank=True, verbose_name=u'邮箱')
    website = models.URLField(blank=True, verbose_name=u'个人网站')

    def __unicode__(self):
        return u'%s' % (self.name)

class Article(models.Model):
    """docstring for Article"""
    caption = models.CharField(max_length=30, verbose_name=u'标题')
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name=u'发表时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')
    viewCount = models.IntegerField(auto_created=1,default=0,verbose_name='浏览次数')
    author = models.ForeignKey(Author, verbose_name=u'作者')
    category = models.ForeignKey(Category, blank=True, verbose_name=u'主分类')
    subcategory = models.ForeignKey(SubCategory,blank=True,verbose_name=u'子分类')
    content = models.TextField(verbose_name=u'内容')

