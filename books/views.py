from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book

# Create your views here.
def home(request):
    return render(request, "books/home.html")

class BookListView(ListView):
    model = Book
    template_name = 'books/main.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/detail.html'