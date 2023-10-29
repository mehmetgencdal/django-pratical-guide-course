from audioop import avg
from django.shortcuts import get_object_or_404, render
from .models import Book
from django.db.models import Avg

# Create your views here.
def index(request):
    
    books = Book.objects.all().order_by("-rating")
    
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    
    context = {
                "books": books,
                "total_number_of_books": num_books,
                "avg_rating": avg_rating["rating__avg"]
               }
    
    return render(request, "book_outlet/index.html", context=context)


def book_details(request, id):
    
    book = get_object_or_404(Book, pk=id)
    
    context = {
                "title": book.title,
                "author": book.author,
                "rating": book.rating,
                "is_bestselling": book.is_bestselling,
              }
    
    return render(request, "book_outlet/book_detail.html", context=context)