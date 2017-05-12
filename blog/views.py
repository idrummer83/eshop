from django.contrib.auth.models import User
from django.urls.base import reverse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.utils.text import slugify
from transliterate.utils import slugify as trans_slugify

from .forms import PostForm
from .models import Post


def details(request, date, slug):
    post = get_object_or_404(Post, slug=slug, date=date)
    return render(request, 'post_detail.html', {
        'post': post
    })

def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts':posts})


def add_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = form.cleaned_data['user']
            # post.user = request.user
            post.slug = trans_slugify(post.name) or slugify(post.name)
            post.save()
            return redirect(reverse('posts'))
    return render(request, 'add_post.html', {
        'form': form
    })

def edit_post(request, date, slug):
    post = get_object_or_404(Post, slug=slug, date=date)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post, )
        if form.is_valid():
            form.save()
            return redirect(reverse('posts'))
    return render(request, 'edit_post.html', {'form': form})
