
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from blog.forms import CommentForm

# Create your views here.
def index(request):
    # top 10
    posts = Post.objects.all()[:10]
    context = {'posts': posts}
    return render(request, 'blog/index.html', context=context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
   
    if request.user.is_active:
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                return redirect(request.path_info)
        else:
            comment_form = CommentForm()
    else:
        comment_form = None
    
    context = {'post': post, "comment_form": comment_form}
    return render(request, "blog/post-detail.html", context=context)


def test(request):
    test = {1: "a", 2:"b", 3: "c"}
    return render(request, 'blog/test.html', context = {"test": test})

def get_ip(request):
    from django.http import HttpResponse
    return HttpResponse(request.META['REMOTE_ADDR'])