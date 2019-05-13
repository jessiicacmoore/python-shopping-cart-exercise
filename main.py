from classes.product import Product
from classes.cart import ShoppingCart

cart = ShoppingCart()

non_taxable = 0
taxable = 0.13
imported = 0.20

blouse = Product('Blouse', 24.00, taxable)
t_shirt = Product('T Shirt', 15.75, non_taxable)
jeans = Product('Jeans', 51.50, imported)


# cart.add_to_cart(blouse)

cart.add_to_cart(jeans)

# cart.add_to_cart(t_shirt)

# cart.remove_from_cart(jeans)


print(cart)
cart.print_receipt()
print(cart.find_most_expensive())