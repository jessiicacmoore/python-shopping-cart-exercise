from classes.product import Product

class ShoppingCart:
  def __init__(self):
    self.cart = []

  def __str__(self):
    return f"{len(self.cart)} items in your cart"

  def add_to_cart(self, to_append):
    self.cart.append(to_append)

  def remove_from_cart(self, to_remove):
    self.cart.remove(to_remove)

  def calculate_sub_total(self):
    sub_total = 0
    for item in self.cart:
      sub_total += item.base_price * item.quantity
    return sub_total

  def calculate_total(self):
    total = 0
    for item in self.cart:
      total += (item.base_price * item.quantity) * (1 + item.tax_rate)
    return total

  def find_most_expensive(self):
    sorted_list = sorted(self.cart, key=lambda product: product.base_price)
    return "The most expensive item on your list is: {} at ${:.2f}".format(sorted_list[-1].name, sorted_list[-1].base_price)

  def print_receipt(self):
    print()
    print('Your Receipt')
    print()
    for item in self.cart:
      print("{}.............{:.2f}".format(item.name, item.base_price))
    print('-------------------------------')
    print("Sub Total:..........{:.2f}".format(self.calculate_sub_total()))    
    print("Total:..............{:.2f}".format(self.calculate_total()))
    print()
    