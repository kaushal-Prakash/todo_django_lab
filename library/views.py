from django.shortcuts import render, redirect
from .models import Book, Publisher, Author
from .forms import BookForm, PublisherForm, AuthorForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'publisher.html', {'publishers': publishers})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author.html', {'authors': authors})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def add_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publisher_list')
    else:
        form = PublisherForm()
    return render(request, 'add_publisher.html', {'form': form})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})
