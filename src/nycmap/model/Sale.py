class Sale:

    def __init__(self, salePrice, saleDate, buildingCode, buildingClassPresent, buildingClassAtSale):

        self.salePrice = salePrice
        self.saleDate = saleDate
        self.buildingCode = buildingCode
        self.buildingClassPresent = buildingClassPresent
        self.buildingClassAtSale = buildingClassAtSale

    def printInfo():
        print("Sale price: %s, Sale date: %s, Building code: %s"
          % (salePrice, saleDate, buildingCode))
