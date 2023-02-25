from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post
# Create your views here.


def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts})



def post_detail(request, slug):
    """ We make use of the get_object_or_404 shortcut which will automatically 
        return a 404 Not Found response if the requested object isn’t found in 
        the database:
    """
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {"post": post})