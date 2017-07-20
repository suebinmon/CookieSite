from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, PostForm

# Create your views here.
def index(request):
	post_list = Post.objects.all()
	return render(request, 'board/post_list.html', {
		'post_list': post_list,
		})

def intro(request):
	return render(request, 'board/intro.html')

def QnA(request):
	return render(request, 'board/QnA.html')

def Main(request):
	return render(request, 'board/Main.html')

def lock(request):
	return render(request, 'board/lock.html')

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'board/post_detail.html', {
		'post': post,
		})


@login_required
def post_new(request):
	if request.method=="GET":
		form = PostForm()
	elif request.method=="POST":
		form = PostForm(request.POST, request.FILES)

		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			post.save()
			return redirect(post,pk=post.pk)
	return render(request, 'board/post_form.html',{
		'form':form,
		})


@login_required
def post_edit(request, pk):
	post=get_object_or_404(Post, pk=pk)
	if request.method=="POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			post.save()
			return redirect(post,pk=post.pk)
	else:
		form=PostForm(instance=post)
	return render(request,'board/post_form.html',{
		'form':form,
		})



@login_required
def post_delete(request, pk):
	post=get_object_or_404(Post, pk=pk)
	if post.author != request.user:
		return redirect('index')

	if request.method=='POST':
		post.delete()
		return redirect('index')
	return render(request, 'board/post_confirm_delete.html', {
		'post':post,
	})


@login_required
def comment_new(request, post_pk):
	post = get_object_or_404(Post, pk=post_pk)

	if request.method == 'POST':
		form = CommentForm(request.POST, request.FILES)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.author = request.user
			comment.save()
			return redirect('board:post_detail', post.pk)
	else:
		form = CommentForm()
	return render(request, 'board/comment_form.html', {
		'form':form,
		})



@login_required
def comment_edit(request, post_pk, pk):
	
	comment = get_object_or_404(Comment, pk=pk)
	if comment.author != request.user:
		return redirect(comment.post)

	if request.method == 'POST':
		form = CommentForm(request.POST, request.FILES, instance=comment)
		if form.is_valid():
			comment = form.save()			
			return redirect(comment.post)
	else:
		form = CommentForm(instance=comment)
	return render(request, 'board/comment_form.html', {
		'form':form,
		})



@login_required
def comment_delete(request, post_pk, pk):
	
	comment = get_object_or_404(Comment, pk=pk)
	if comment.author != request.user:
		return redirect(comment.post)

	if request.method == 'POST':
		comment.delete()
		return redirect(comment.post)

	return render(request, 'board/comment_confirm_delete.html', {
		'comment':comment,
		})