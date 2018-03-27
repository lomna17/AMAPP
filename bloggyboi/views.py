from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "bloggyboi/post_list.html", {"posts": posts})

def search(request):
    search_query = request.GET.get('search_box', None)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(search_query)
    return render(request, "bloggyboi/search.html", {"posts": posts})
