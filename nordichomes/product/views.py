from django.shortcuts import render, get_object_or_404
# Importa o modelo Product do mesmo diretório (pacote) onde este arquivo está localizado.
from .models import Product
# Define uma função de visualização chamada 'product'.
def product(request, slug):
    # Realiza uma consulta ao banco de dados para obter um objeto Product com base no slug fornecido na URL.
    # Se não houver correspondência, o método 'get_object_or_404' lançará uma exceção 'Product.DoesNotExist'.
    product = get_object_or_404(Product, slug=slug)
    # Utiliza a função 'render' para criar a resposta HTTP.
    # Esta função renderiza o template 'product/product.html' e passa o objeto 'Product' para o contexto.
    return render(request, 'product/product.html', {'product': product})

