
class ZipCode:

  def __init__(self, sale, data):
    self.sales = [sale]
    self.zipCode = sale.zipCode
    self.data = data
    self.long = self.data.lng
    self.lat = self.data.lat
    

  def append(self, sale):
    if sale.zipCode != self.zipCode:
      raise Exception('wrong sale (%s) being added to zipCode:%s', (sale.zipCode, self.zipCode))
    self.sales.append(sale)


  def print(self):
    print("zipCode: %s. %s" % (self.zipCode, self.data))
    for sale in self.sales:
      sale.print()

    
