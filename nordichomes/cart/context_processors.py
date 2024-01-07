from .cart import Cart

def cart(request):
    # Importa a classe 'Cart' do módulo 'cart'.
    # Define uma função de contexto chamada 'cart' que aceita um objeto 'request' como parâmetro.

    # Retorna um dicionário de contexto com a chave 'cart' associada a uma instância da classe 'Cart'
    # inicializada com o objeto 'request'. Isso permite que o carrinho de compras seja acessado nos templates.
    return {'cart': Cart(request)}