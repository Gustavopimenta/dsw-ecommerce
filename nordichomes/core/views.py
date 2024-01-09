from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q # classe Q é uma poderosa ferramenta no Django para realizar consultas complexas no banco de dados, especialmente quando você precisa combinar múltiplas condições lógicas
from django.shortcuts import render, redirect

from product.models import Product, Category

from .forms import SignUpForm

def frontpage(request):
    products = Product.objects.all()[0:8]
    
    return render(request, 'core/frontpage.html',{'products': products})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            login(request, user)

            return redirect('/')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html')

@login_required
def myaccount(request):
    return render(request, 'core/myaccount.html')


@login_required
def edit_myaccount(request):
    if request.method == 'POST': # Se a requisição é do tipo POST (submissão de formulário)
        user = request.user  # Obtém o usuário associado à requisição (usuário autenticado)
        user.first_name = request.POST.get('first_name') # Atualiza os dados do usuário com os valores recebidos do formulário POST
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.save()# Salva as alterações no banco de dados
        # Redireciona para a página 'myaccount'
        return redirect('myaccount')
    return render(request, 'core/edit_myaccount.html') # Se a requisição não for do tipo POST, renderiza a página de edição do perfil
    

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
    
