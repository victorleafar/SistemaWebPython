from django.shortcuts import render, HttpResponse
from .models import Produto

def book_list_view(request):
    produto = Produto.objects.all()
    template = 'crudapp/book-list.html'
    return render(request, template, {'Produtos': produto})
