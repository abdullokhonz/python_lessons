class Products:
    def __init__(self, name: str, price: int, count: int, category: str):
        self.name, self.price, self.count, self.category = name, price, count, category

    def return_products(self):
        return {'name': self.name, 'price': self.price, 'count': self.count, 'category': self.category}


class Electronics(Products):
    pass


class Clothes(Products):
    pass


class Accessories(Products):
    pass
