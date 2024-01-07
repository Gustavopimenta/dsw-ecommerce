from django.db.models import Q
from django.shortcuts import render

from product.models import Product, Category

def frontpage(request):
    products = Product.objects.all()[0:8]
    
    return render(request, 'core/frontpage.html',{'products': products})

def shop(request): # Obtém todas as categorias e produtos do banco de dados
    categories = Category.objects.all() 
    products = Product.objects.all()
    # Obtém a categoria ativa a partir dos parâmetros da URL
    active_category = request.GET.get('category','')
     # Cria um contexto contendo as categorias, produtos e a categoria ativa
    
    if active_category:
        products = products.filter(category__slug=active_category)
    query = request.GET.get('query',)
    
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    context = {
        'categories': categories, 
        'products': products,    
        'active_category': active_category
    }
    # Renderiza a página HTML utilizando o template 'core/shop.html' e o contexto criado
    return render(request, 'core/shop.html', context)
    
