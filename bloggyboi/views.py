from django.shortcuts import render
from .models import Post
from .forms import DropDown
#from django.http import HttpResponseRedirect
from django.utils import timezone

# Create your views here.
def post_list(request):
    if request.method == "POST":
        form = DropDown(request.POST)
    else:
        form = DropDown()
    posts = Post.objects.order_by('published_date')
    return render(request, "bloggyboi/post_list.html", {"posts": posts, "form": form})

def search(request):
    search_query = request.GET.get('search_box', None)
    posts = Post.objects.order_by(search_query)
    return render(request, "bloggyboi/search.html", {"posts": posts})

def get_field(request):
    if request.method == "POST":
        form = DropDown(request.POST)
    else:
        form = DropDown()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'bloggyboi/formTest.html', {"posts": posts, 'form': form})