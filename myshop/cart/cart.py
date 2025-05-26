from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart:
    def __init__(self, request):
        """Инициализировать корзину"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            #сохранить корзину в сеансе
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

        def add(self, product, quantity=1, override_quantity = False):
            """Добавить товар к корзину, либо обновить его количество"""
            product_id = str(product.id)
            if product_id not in self.cart:
                self.casrt[product_id] = {
                    "quantity": 0,
                    "price": str(product.price)
                }
                if override_quantity:
                    self.cart[product_id]["quantity"] = quantity
                else:
                    self.cart[product_id]["quantity"] += quantity

        def save(self):
            #пометить сеанс как измененный
            #что бы обеспечить его сохранение
            self.session.modified = True


        def remove(self):
            """Удалить товар из корзины"""
            product_id = str(product.id)
            if product_id in self.cart:
                del self.cart[product_id]
                self.save()

        def __iter__(self):
            """
            Прокрутить товарные позиции корзины в цикле
            и получит товары из БД
            """
            product_ids = self.cart.keys()
            #получить объекты product и добавить их в корзину
            products = Product.objects,filter(id__in=product_ids)
            cart = self.cart.copy()
            for product in products:
                cart[str(product.id)]["product"] = product
            for item in cart.values():
                item["price"] = Decimal(item["price"])
                item["total_price"] = item["price"] * item["quantity"]
                yield item

        def __len__(self):
            """Подсчитать все  товарные в корзине"""
            return sum(item["quantity"] for item in self.cart.values())

        def get_total_price(self):
            return sum(
                Decimal(item["price"] * item["quntity"])
                for item in self.cart.values()
            )

        
        def clear(self):
            #удалить корзину из сеанса
            del delf.session[settings.CART_SESSION_ID]
            self.save()