__author__ = 'lac'
import datetime
from django.http import HttpResponse,Http404
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from myblog.models import  BlogPost
from django.http import Http404, HttpResponseRedirect
from django.views.decorators.cache import cache_page
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import never_cache
from django.contrib.syndication.views import Feed
from django.views.decorators.csrf import csrf_exempt
from myblog.forms import  BlogForm,TagForm
import time

@cache_page(60 * 15)
@cache_control(public=True, must_revalidate=True, max_age=1200)
def index_page(request):
    '''这个view的功能是显示主页，并实现分页功能。
    cache_page装饰器定义了这个view所对应的页面的缓存时间。
    cache_control装饰器告诉了上游缓存可以以共缓存的形式缓存内容，并且告诉客户端浏览器，这个
    页面每次访问都要验证缓存，并且缓存有效时间为1200秒。
    '''
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

    posts = BlogPost.objects.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        posts_of_page = paginator.page(page)
    except PageNotAnInteger:
        posts_of_page = paginator.page(1)
    except EmptyPage:
        posts_of_page = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'posts_of_page': posts_of_page}, )

@never_cache
def blog_show(request, id=''):
    '''这个view的作用是显示博客的正文内容。
    这个view会根据段落、图片、代码对象的sequence属性的值进行排序，
    生成一个最终显示列表返回给模版进行渲染。
    为了实现评论后刷新页面能马上看到评论信息，加入了nerver_cache装饰器使得这个
    view所对应的页面不被缓存。
    '''

    def create_post_objects(objects, output_dict):
        for i in range(len(objects)):
            output_dict[int('%d'%objects[i].sequence)] = objects[i]

    try:
        post = BlogPost.objects.get(id=id)
    except BlogPost.DoesNotExist:
        raise Http404
    blog_post_list = {}

    photos = post.photo_set.all()
    codes = post.code_set.all()
    paragraphs = post.paragraph_set.all()

    create_post_objects(photos, blog_post_list)
    create_post_objects(codes, blog_post_list)
    create_post_objects(paragraphs, blog_post_list)

    context_list = []
    for x in sorted(blog_post_list):
        context_list.append(blog_post_list[x])

    rs = {}
    try:
        next_post = BlogPost.objects.get(id=int(id)+1)
        rs['next'] = next_post
    except BlogPost.DoesNotExist:
        rs['next'] = 0
    try:
        pre_post = BlogPost.objects.get(id=int(id)-1)
        rs['pre'] = pre_post
    except BlogPost.DoesNotExist:
        rs['pre'] = 0

    return render(
        request, 'blog_show.html', {
          'post': post, 'context_list': context_list, 'next_post': rs['next'],
          'pre_post': rs['pre'],
        },
    )

def blog_show_comment(request, id=''):
    blog = BlogPost.objects.get(id=id)
    return render('blog_comments_show.html', {"blog": blog})

def RSS_url(request):
    return HttpResponse('haoba')

def add_blog(request):
    form = BlogForm()
    tag = TagForm()
    return render_to_response('blog_add.html')

@csrf_exempt
def add_blog_action(request):
    if 'title' in request.POST and 'para' in request.POST:
        title = request.POST['title']
        summary = request.POST['para']
        if 'tags' in request.POST:
            tag = request.POST['tags']
        blognew = BlogPost(title =title,author='lac',summary=summary,timestamp=time.strftime('%Y-%m-%d',time.localtime(time.time())))
        blognew.save()
        return render_to_response("errors.html",{"message":"success"})
    else:
       return render_to_response('add_blog.html',{"message": "请输入内容"})
