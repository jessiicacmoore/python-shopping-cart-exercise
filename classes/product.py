

class Product:
  def __init__(self, name, base_price, tax_type):
    self.name = name
    self.base_price = base_price
    self.tax_rate = tax_type

  def __str__(self):
    return "Name: {}\nBase Price: ${:.2f}\nTax Rate: {}%".format(self.name, self.base_price, int(self.tax_rate * 100))

  def calculate_total_price(self):
    return self.base_price * (1 + self.tax_rate)