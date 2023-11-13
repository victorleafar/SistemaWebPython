from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm
from django.core.paginator import Paginator

# Create your views here.
def produtoList(request):
    produtos_list = Produto.objects.all() # busca todos os produtos
    paginator = Paginator(produtos_list, 10) # cria um paginador para 10 produtos por página

    page = request.GET.get('page') # pega o número da página da URL
    produtos = paginator.get_page(page) # busca os produtos da página atual

    return render(request, 'produto_list.html', {'produtos': produtos})

def produtoCreate(request):  
    if request.method == "POST":  
        form = ProdutoForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('produto_list')  
            except:  
                pass  
    else:  
        form = ProdutoForm()  
    return render(request,'produto_create.html',{'form':form})  

def produtoUpdate(request, id):  
    produto = Produto.objects.get(id=id)
    print(f"ABACAXI: {produto.descricao} {produto.preco}")
    if request.method == "POST":  
        print("passou aqui 2")
        form = ProdutoForm(request.POST, instance=produto)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/produto_list')  
            except Exception as e: 
                pass    
    print("passou aqui 1")
    form = ProdutoForm(instance=produto)
    return render(request,'produto_update.html',{'form':form})  

def produtoDelete(request, id):
    produto = Produto.objects.get(id=id)
    try:
        produto.delete()
    except:
        pass
    return redirect('produto_list')