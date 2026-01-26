from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Book
from .forms import BookForm
from django.contrib import messages

# Create your views here.
def index(request):
    book_list = Book.objects.all()
    context = {
        'book_list':book_list
    }
    return render(request,'Store/index.html',context)

@login_required
def details(request,id):
    book_list = Book.objects.all()
    book = Book.objects.get(id = id)
    context = {'book':book,'book_list':book_list}
    return render(request,'Store/details.html',context)

@login_required
def add_book(request):
    form = BookForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Store:index')
    context={'form':form}
    return render(request,'Store/bookform.html',context)

@login_required
def update_book(request,id):
    book = Book.objects.get(id = id)
    form = BookForm(request.POST or None, instance = book)
    if form.is_valid():
        form.save()
        return redirect('Store:index')
    context = {'form':form}
    return render(request,'Store/bookform.html',context)

@login_required
def delete_book(request,id):
    book = Book.objects.get(id = id)
    if request.method == 'POST':
        book.delete()
        return redirect('Store:index')
    return render(request,'Store/delete.html')
