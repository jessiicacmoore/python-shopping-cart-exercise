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
      sub_total += item.base_price
    return sub_total

  def calculate_total(self):
    total = 0
    for item in self.cart:
      total += item.base_price * (1 + item.tax_rate)
    return total