from django.shortcuts import render,redirect,HttpResponse
from .models import Post
from .forms import *

# Create your views here.
def postdata(request):
    post_data=Post.objects.all()
    
    context={'post_data':post_data}
    return render(request,'post.html',context)

def post_item(request):
    post_item=Post.objects.all()
    context={'post_item':post_item}
    return render(request, 'post_item.html',context)

def createpost(request):
  
    if request.method=="POST":
        title=request.POST.get('title')
        body=request.POST.get('body')
        photo=request.FILES.get('photo')
        print(title)
        print(body)
        print(photo)
        query=Post.objects.create(title=title,post_body=body,photo=photo)
        print('Success...........')
        return redirect("/post")
    return render(request,'createpost.html')


def createform(request):
    
    fm=PostModelForm()
    if request.method=="POST":
        fm=PostModelForm(request.POST,request.FILES)
        if fm.is_valid():
            print(fm)
            fm.save()
          
            return redirect('/post')
        else:
           
            return HttpResponse('Error')
    return render(request,'createpost.html',{'fm':fm})

def postdetail(request,id):
    data=Post.objects.filter(id=id)
    
    context={"data":data}
    return render(request,'postdetails.html',context)