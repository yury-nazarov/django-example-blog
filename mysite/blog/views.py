from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.

from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    posts = Post.published.all()
    # Постраничная разбивка с 3 постами на страницу
    paginator = Paginator(posts, 3)
    # page - номер страницы из get запроса,
    # 1 - номер страницы по умолчанию если page пута
    page_number = request.GET.get('page', 1)
    try:
        posts_per_page = paginator.page(page_number)
    except EmptyPage:
        # Возвращаем последнюю страницу
        posts_per_page = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        # Если передали не число, а строку, вернем на первую страницу
        posts_per_page = paginator.page(1)

    return render(request,
                  'blog/post/list.html',
                  {'posts': posts_per_page})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    return render(request,
                  'blog/post/detail.html',
                  {'post': post})

