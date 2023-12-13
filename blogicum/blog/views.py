from datetime import datetime

from django.shortcuts import render, get_object_or_404

from blog.models import Post, Category
from blogicum.constants import POST_ON_MAIN_AMOUNT

CURRENT_DATE = datetime.now()


def get_post_list(query):
    return query.select_related(
        'category', 'author', 'location'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=CURRENT_DATE
    )


def index(request):
    template = 'blog/index.html'
    post_list = get_post_list(Post.objects)[:POST_ON_MAIN_AMOUNT]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(get_post_list(Post.objects), pk=post_id)
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(Category.objects.filter(
        is_published=True,
    ), slug=category_slug)
    post_list = category.category.filter(
        is_published=True,
        pub_date__lte=CURRENT_DATE
    )
    context = {'category': category,
               'post_list': post_list}
    print(context)
    return render(request, template, context)
