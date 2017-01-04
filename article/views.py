from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from django.shortcuts import render_to_response
import datetime
from django.http import Http404


# Create your views here.

def home2(request):
    return HttpResponse("qingwa")


def detail(request, id):
    try:

        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render_to_response('article/post.html', {'post': post})


def home(request):
    post_list = Article.objects.all()
    # if not request.user.is_authenticated():
    #     print 'not login'
    # print 'login'
    user = request.user
    return render_to_response('article/home.html', locals())
