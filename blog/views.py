from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post, Comment, Leaguetable, Solvedproblem, Gamesetproblem, Gamesetinfo
from .forms import PostForm, CommentForm, LeaguetableForm, GameForm, ProblemForm, HandleForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(posts,4)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', {'posts': contacts})
    #return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_about_me(request):
    return render(request, 'blog/post_about_me.html')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            """post.published_date = timezone.now()"""
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            """post.published_date = timezone.now()"""
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)

def football_list(request):
    leaguetable = Leaguetable.objects.filter()
    #leaguetable = get_object_or_404(Leaguetable, pk=pk)
    return render(request, 'blog/football_list.html', {'leagueTable': leaguetable})

def home(request):
    return render(request, 'blog/home.html' )

def pinterest(request):
    return render(request, 'blog/pinterest.html')

def project(request):
    return render(request, 'blog/project.html')

def problem_game(request):
    return render(request, 'blog/problem_game.html')

def new_game(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.save()
            return redirect('add_problem')
    else:
        form = GameForm()
    return render(request, 'blog/new_game.html', {'form': form})

def add_problem(request):
    problem = Gamesetproblem.objects.filter().order_by('rule_num')
    if request.method == "POST":
        form = ProblemForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.save()
            return redirect('add_problem')
    else:
        form = ProblemForm()
    return render(request, 'blog/add_problem.html', {'form': form, 'problem':problem})

def show_game(request):
    if request.method == "POST":
        form = HandleForm(request.POST)
        problem = Gamesetproblem.objects.get(handle="Martian")
        return redirect('show_game')
    else:
        form = HandleForm()
    return render(request, 'blog/show_game.html',{'form': form,})
