from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Book
from .forms import BookForm
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
#def index(request):
    
    #book_list = Book.objects.all()
    #context = {
        #'book_list':book_list
    #}
    #return render(request,'Store/index.html',context)

class IndexClassView(ListView):
    model = Book
    template_name = "Store/index.html"
    context_object_name = 'book_list' 


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
            form.instance.added_by = request.user
            form.save()
            return redirect('Store:index')
    context={'form':form}
    return render(request,'Store/book_form.html',context)

#class BookCreateView(CreateView):
    #automatically looks for book_form.html and renders it
    #model = Book
    #fields=['book_name','author','publisher','edition','genre','image']
    #redirect url is mentioned in Book model definition

@login_required
def update_book(request,id):
    book = Book.objects.get(id = id)
    form = BookForm(request.POST or None, instance = book)
    if form.is_valid():
        if request.user.is_superuser or book.added_by.id == request.user.id:
            form.save()
        return redirect('Store:index')
    context = {'form':form}
    return render(request,'Store/book_form.html',context)

#class BookUpdateView(UpdateView):
    #model = Book
    #fields=['book_name','author','publisher','edition','genre','image'] 
    #template_name_suffix = "_form"

@login_required
def delete_book(request,id):
    book = Book.objects.get(id = id)
    if request.method == 'POST':
        if request.user.is_superuser or book.added_by.id == request.user.id:
            book.delete()
        return redirect('Store:index')
    return render(request,'Store/book_confirm_delete.html')


#class BookDeleteView(DeleteView):
    #model = Book
    #success_url = reverse_lazy("Store:index")
