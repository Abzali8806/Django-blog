from asyncio import sleep
from django.shortcuts import render

from browser.models import Space
from .forms import CreatePostForm
from .models import Post


def frontpage_view(request):
    posts = Post.objects.all()
    return render(request, 'blog/frontpage.html', {'posts': posts})


def space_detail_view(request, space_slug):
    space = Space.objects.get(slug=space_slug) # get all - then filter inside template
    posts = Post.objects.all()
    
    print(space_slug)
    
    for post in posts:
        if space_slug == post.spaceslug:
            print(post.title)
            print(post.postslug)
    context = {
        "space": space,
        "posts": posts
    }
    return render(request, 'blog/space_detail.html', context)

def post_detail_view(request, space_slug, post_slug):
    post = Post.objects.get(post_slug=post_slug)

    # print(post_slug)
    context = {
        "post": post
    }

    # print(post)
    return render(request, 'blog/post_detail.html', context)


def create_post_view(request, space_slug):
    post_form = CreatePostForm(request.POST or None)
    if request.method == 'POST':
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.space_slug = space_slug
            new_post.save()
    context = {
        "form": post_form
    }
    return render(request, 'blog/create_post.html', context)
