from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Author, Category, Post
from .forms import AuthorForm, CategoryForm, PostForm, SearchForm

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm()
    return render(request, 'blog/add_author.html', {'form': form})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'blog/add_category.html', {'form': form})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

def search_post(request):
    form = SearchForm()
    results = None
    if 'search_term' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            search_term = form.cleaned_data['search_term']
            results = Post.objects.filter(title__icontains=search_term)
    return render(request, 'blog/search_post.html', {'form': form, 'results': results})
