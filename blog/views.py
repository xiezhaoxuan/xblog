# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response,render
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect,HttpResponse,HttpResponseNotFound
from blog.models import Article, Author, Category,SubCategory
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.template import loader


def blog_list(request):
    blog_list = Article.objects.all().order_by('-publish_time')
    categories = Category.objects.all()

    paginator = Paginator(blog_list, 5)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    return render(request, 'blog_list.html',
                 {'blogs':blogs,'categories':categories})

def blog_del(request, id=""):
    try:
        blog = Article.objects.get(id=id)
    except Exception:
        raise Http404
    if blog:
        blog.delete()
        return HttpResponseRedirect("/blog/bloglist/")
    blogs = Article.objects.all()
    return render_to_response("blog_list.html", {"blogs": blogs})


def blog_show(request, id=''):
    try:
        blog = Article.objects.get(id=id)
        categories = Category.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render_to_response("blog_show.html",
           {"blog": blog, "categories": categories})

def blog_category(request, id=''):
    categories = Category.objects.all()
    category = Category.objects.get(id=id)
    blogs = Article.objects.filter(category=category)
    return render_to_response("blog_category_filter.html", {"blogs": blogs, "category": category, "categories": categories})


def blog_show_comment(request, id=''):
    blog = Article.objects.get(id=id)
    return render_to_response('blog_comments_show.html', {"blog": blog})


def blog_search(request):
    tags = Tag.objects.all()
    if 'search' in request.GET:
        search = request.GET['search']
        blogs = Article.objects.filter(caption__icontains=search).order_by('-publish_time')
        categories = Category.objects.all()
        return render_to_response('blog_search.html',
            {"blogs": blogs, "tags": tags, "categories": categories}, context_instance=RequestContext(request))
    else:
        blogs = Article.objects.order_by('-id')
        return render_to_response("blog_list.html", {"blogs": blogs, "tags": tags},
            context_instance=RequestContext(request))


def GetCategory(request,id=''):
    if id == '001':  #从数据库中提取主类与子类的对应关系并返回
        subCategories = SubCategory.objects.values('id','category_id')
        subCategorieList = "["
        for subCategorie in subCategories:
            subCategorieList += '{"' + str(subCategorie['category_id']) + '":"' + str(subCategorie['id']) + '"}'
            # subCategorieList.append([int(subCategorie['category_id']),int(subCategorie['id'])])
        subCategorieList += "]"
        return HttpResponse(subCategorieList)
    else:
        return HttpResponseNotFound('没有')