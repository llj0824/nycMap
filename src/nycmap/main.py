import sys
import geopandas
import pandas
import matplotlib.pyplot as matlibPlot
import os
from util import FileReader
from model import Sale, ZipCode
from uszipcode import SearchEngine, SimpleZipcode

#graph size
mapSize = (150,150)
mapColor = '#3B3C6E'

# column names converted by Pandas Dataframe
buildingCategoryCol = '_3'
buildingClassPresentCol = '_8'
zipCode = '_11'
buildingClassAtSaleCol = '_19'
salePriceCol = '_20'
saleDateCol = '_21'

WORKING_DIRECTORY = os.getcwd()
CSV_FILE = 'data/rollingsales_queensSample.csv'
NYC_ZIPCODE_GEOJSON = 'data/newyork.zipcode.geojson'


def main(args):
    df = FileReader.parseCsvFile(CSV_FILE)
    sales = populateSales(df)
    zipCodes = populateZipcodes(sales, SearchEngine())

    # Create map of new york
    mapOfNyc = geopandas.read_file(NYC_ZIPCODE_GEOJSON)
    mapOfNyc.plot(figsize=mapSize, color= mapColor)
    matlibPlot.show()
    # Create map of new york (GeoJson)
    # construct GeoJson (Json file)




    print("End world")

def populateSales(dataFrame):
    sales = []
    for tup in dataFrame.itertuples():
        row = tup._asdict()
        sale = Sale.Sale()
        sale.salePrice = row[salePriceCol]
        sale.saleDate = row[saleDateCol]
        sale.buildingCode = row[buildingCategoryCol]
        sale.buildingClassPresent = row[buildingClassPresentCol]
        sale.buildingClassAtSale = row[buildingClassAtSaleCol]
        sale.zipCode = row[zipCode]
        sales.append(sale)
    return sales

def populateZipcodes(sales, zipCodeDataEngine):
    zipcodeToSaleDict = {}
    for sale in sales:
        if(sale.zipCode in zipcodeToSaleDict):
            zipcodeToSaleDict[sale.zipCode].append(sale)
        else:
            zipCodeInfo= zipCodeDataEngine.by_zipcode(int(sale.zipCode))
            zipcodeToSaleDict[sale.zipCode] = ZipCode.ZipCode(sale, zipCodeInfo)
    # return list of zipCode, not dict
    return zipcodeToSaleDict.values()


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main(sys.argv[:])
