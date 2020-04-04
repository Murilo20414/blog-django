from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    more_access_posts = Post.objects.filter(access__gte=0).order_by('-access')[:3]
    
    return render(request, 'blog/post_list.html', {'posts': posts, 'more_access_posts' : more_access_posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.access += 1
    post.save()
    return render(request, 'blog/post_detail.html', {'post' : post})
    
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk = post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form' : form})

