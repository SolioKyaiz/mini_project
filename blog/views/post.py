from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

from blog.forms import CreatePostForm
from blog.models import Post
from blog.forms import CreatePostForm

@login_required()
def post_list(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'blog/post_list.html',context)

@login_required
def post_detail(request,pk):
    post = get_object_or_404(Post, pk = pk)
    post_categories = post.category.all()
    comments = post.comments.all()
    context = {'post': post, 'comments': comments,'post_categories':post_categories,'user':request.user}
    return render(request,'blog/post_detail.html',context)

@login_required()
def post_create(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form .is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = CreatePostForm()
    return render(request,'blog/post_create.html',{'form':form})

@login_required()
def post_edit(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post-detail', pk=pk)
    else:
        form = CreatePostForm(instance=post)
    return render(request,'blog/post_edit.html',{'form':form,'post': post})

@login_required()
def post_delete(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect('blog:post-list')




