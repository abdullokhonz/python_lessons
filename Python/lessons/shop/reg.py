class Registration:
    available_products: dict = {}
    available_categories: dict = {'electronics': 0, 'clothes': 0, 'accessories': 0}
    transactions: list = []

    def __init__(self, product):
        self.available_products = product
        self.available_categories[self.available_products['category']] += self.available_products['count']
        self.transactions.append(f'Добавлен новый товар: {self.available_products['name']}')

    def sell_product(self):
        if self.available_products['count'] != 0:
            self.available_products['count'] -= 1
            self.available_categories[self.available_products['category']] = self.available_products['count']
            self.transactions.append(f'Товар продан: {self.available_products['name']}')
        else:
            self.available_products = {}

    def return_available_products(self):
        try:
            return (f'Name: {self.available_products['name']}, Price: {self.available_products['price']}, '
                    f'Count: {self.available_products['count']}, Category: {self.available_products['category']}.')
        except KeyError:
            return 'Все товары проданы!'

    def return_available_categories(self, category):
        try:
            return f'{category.title()}: {self.available_categories[category]}.'
        except KeyError:
            return 'В этой категории больше нет товаров!!'

    def return_transactions(self):
        return self.transactions
