from django.shortcuts import render
from .models import Post

# Create your views here.
def postdata(request):
    post_data=Post.objects.all()
    context={'post_data':post_data}
    return render(request,'post.html',context)

def post_item(request):
    post_item=Post.objects.all()
    context={'post_item':post_item}
    return render(request, 'post_item.html',context)