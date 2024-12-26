import products
import reg

products = products.Electronics('Phone', 250, 2, 'electronics')

reg = reg.Registration(products.return_products())

print(reg.return_available_products())

reg.sell_product()
print(reg.return_available_products())

reg.sell_product()
print(reg.return_available_products())

reg.sell_product()
print(reg.return_available_products())

print(reg.return_available_categories('electronics'))

print(*reg.return_transactions(), sep='\n')
