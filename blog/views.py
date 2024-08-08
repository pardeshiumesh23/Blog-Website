from django.shortcuts import render,redirect
from .models import PostModel
from .forms import PostModelForm,PostUpdateForms,CommentForm
from django.contrib.auth.decorators import login_required #login is required for any user before he/she access any page


def index(request):
    posts=PostModel.objects.all()
    return render(request,"blog/index.html",{"posts":posts})

def about(request):
    if request.method == "GET":
        return render(request,'blog/about.html')

@login_required
def createpost(request):
    posts=PostModel.objects.all()
    if request.method =="POST":
        form=PostModelForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog-index')  
    else:        
        form = PostModelForm()
    context = {
        'posts': posts,
        'form':form
    }
    return render(request,'blog/createpost.html',context)

@login_required
def post_details(request,pk):
    post=PostModel.objects.get(id=pk)
    if request.method == "POST":
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = request.user #only login user can comment
            instance.post = post #here this post refer to 2nd line in this function as pk 
            instance.save()
            return redirect ('blog-post-details', pk=post.id) 
    else:
        c_form = CommentForm()
    context={
        'post': post,
        'c_from': c_form,
    }
    return render(request,'blog/post_details.html',context)

@login_required
def post_edit(request,pk):
    post = PostModel.objects.get(id=pk)
    if request.method == "POST":
        form= PostUpdateForms(request.POST,request.FILES,instance=post) #instance=post is used to display info that is already present or prefield
        if form.is_valid():
            form.save()
            return redirect('blog-post-details', pk=post.id) #pk=post.id is used becoz when we go back to post-details pk is required in url
        else:
            print(form.errors)
    else:
        form= PostUpdateForms(instance=post)
    context={
        'post': post,
        'form' : form,
    }
    return render(request,'blog/post_edit.html',context)

@login_required
def post_delete(request,pk):
    post = PostModel.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        return redirect('blog-index')
    context={
        'post' : post,
    }
    return render(request,'blog/post_delete.html',context)

