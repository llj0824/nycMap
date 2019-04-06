class Sale:
    salePrice = None
    saleDate = None
    buildingCode = None
    buildingClassPresent = None 
    buildingClassAtSale = None

    def __init__(self):
        pass

    # def __init__(self, salePrice, saleDate, buildingCode, buildingClassPresent, buildingClassAtSale):
    #     self.salePrice = salePrice
    #     self.saleDate = saleDate
    #     self.buildingCode = buildingCode
    #     self.buildingClassPresent = buildingClassPresent
    #     self.buildingClassAtSale = buildingClassAtSale

    def print(self):
        print("Sale price: %s, Sale date: %s, Building code: %s"
              % (self.salePrice, self.saleDate, self.buildingCode))
