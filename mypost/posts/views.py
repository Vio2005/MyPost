from django.shortcuts import render
from .models import Post

# Create your views here.
def postdata(request):
    post_data=Post.objects.all()
    context={'post_data':post_data}
    return render(request,'post.html',context)
