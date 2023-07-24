from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm


def pagina_inicial(request):
    produtos = Produto.objects.all()
    context = {
        'produtos' : produtos
    }
    return render(request, "pagina_inicial.html",context)

def area_administrativa(request):
    produtos = Produto.objects.all()
    context = {
        'produtos' : produtos
    }
    return render(request, "area_administrativa.html",context)

def produto_detalhes(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'produto_detalhes.html', {'produto': produto}) #pega as infos só do produto clicado




#CRUD PRODUTO

def produto_editar(request, id):
    produto = get_object_or_404(Produto,id=id)
   
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto_listar')
    else:
        form = ProdutoForm(instance=produto)

    return render(request,'form.html',{'form':form})


def produto_remover(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('area_administrativa') 


def produto_criar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProdutoForm()
    else:
        form = ProdutoForm()

    return render(request, "form.html", {'form': form})
     


def produto_listar(request):
    produtos = Produto.objects.all()
    context ={
        'produtos':produtos
    }
    return render(request, "produto_listar.html",context)






