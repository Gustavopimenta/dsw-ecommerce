from django.conf import settings
from product.models import Product

class Cart(object):
    def __init__(self, request):
        # Inicializa a instância do carrinho com base na sessão do usuário.
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        
        # Se não houver um carrinho na sessão, cria um novo carrinho.
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        
        # Atribui o carrinho à instância.
        self.cart = cart
        
    def __iter__(self):
        # Itera sobre os itens no carrinho e associa cada produto ao seu objeto Product correspondente.
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)
            
    def __len__(self):
        # Retorna o número total de itens no carrinho.
        return sum(item['quantity'] for item in self.cart.values())
    
    def save(self):
        # Salva as alterações no carrinho na sessão do usuário.
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
    
    def add(self, product_id, quantity=1, update_quantity=False):
        # Converte o ID do produto para string.
        product_id = str(product_id)
        
        # Se o produto não estiver no carrinho, adiciona com uma quantidade padrão de 1.
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1, 'id': product_id}
        
        # Se update_quantity for True, atualiza a quantidade do produto no carrinho.
        if update_quantity:
            self.cart[product_id]['quantity'] += int(quantity)
            
            # Se a quantidade for zero, remove o produto do carrinho.
            if self.cart[product_id]['quantity'] == 0:
                self.remove(product_id)
        self.save()
    
    def remove(self, product_id):
        # Remove um produto específico do carrinho.
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
