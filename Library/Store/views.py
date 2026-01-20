from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.
def index(request):
    book_list = Book.objects.all()
    context = {
        'book_list':book_list
    }
    return render(request,'Store/index.html',context)

def details(request,id):
    book_list = Book.objects.all()
    book = Book.objects.get(id = id)
    context = {'book':book,'book_list':book_list}
    return render(request,'Store/details.html',context)