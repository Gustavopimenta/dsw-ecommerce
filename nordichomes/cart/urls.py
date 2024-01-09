from django.urls import path

from cart.views import add_to_cart, cart, checkout

urlpatterns = [
    path('', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
]


#path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart')
# Rota para adicionar um produto ao carrinho. 
# O padrão de URL espera um número inteiro após 'add_to_cart/', 
# que será passado como argumento 'product_id' para a função de visualização 'add_to_cart'.
