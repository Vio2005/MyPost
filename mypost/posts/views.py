from django.shortcuts import render
from .models import Post

# Create your views here.
def postdata(request):
    post_data=Post.objects.all()
    context={'post_data':post_data}
    return render(request,'post.html',context)
def postdetail(request,pk):
    data=Post.objects.filter(id= pk)
    getdata=Post.objects.get(id=pk) #single query
    context={'data':data, 'getdata':getdata}
    return render(request,'postdetails.html',context)