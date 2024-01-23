from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator


def post_list(request):
    posts = Post.published.all()
    # Разбивка по 3 поста на одну страницу
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    return render(request,
                  "blog/post/list.html",
                  {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             )
    return render(request,
                  "blog/post/detail.html",
                  {'post': post})
