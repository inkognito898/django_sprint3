from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.db.models import Q
from datetime import datetime


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.values(
        'title', 'location', 'pub_date', 'author'
    ).filter(
        Q(is_published=True) & Q(category__is_published=True)
        & Q(pub_date__lte=datetime.now())
    )
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.now()
    ), pk=post_id)
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.now()
    ), category__slug=category_slug)
    context = {'category': category}
    return render(request, template, context)