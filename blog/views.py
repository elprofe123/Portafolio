from django.shortcuts import render, get_object_or_404  # type: ignore
from .models import Post
# Create your views here.

# pagina de post


def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


def post_detail(request, post_id):
    # toma primero el modelo,Post. y luego el post_id en primary key
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})  # type: ignore
