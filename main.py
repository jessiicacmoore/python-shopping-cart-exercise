from classes.product import Product
from classes.cart import ShoppingCart

cart = ShoppingCart()

blouse = Product('Blouse', 24.00)
t_shirt = Product('T Shirt', 15.75)
jeans = Product('Jeans', 51.50)

print(cart)

cart.add_to_cart(blouse)
print(cart)
print(cart.calculate_sub_total())
print(cart.calculate_total())
cart.add_to_cart(jeans)
print(cart)
print(cart.calculate_sub_total())
print(cart.calculate_total())
cart.add_to_cart(t_shirt)
print(cart)
print(cart.calculate_sub_total())
print(cart.calculate_total())
cart.remove_from_cart(jeans)
print(cart)
print(cart.calculate_sub_total())
print(cart.calculate_total())