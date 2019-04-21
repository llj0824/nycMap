import sys
import geopandas
import pandas
import matplotlib.pyplot as matlibPlot
import os
from util import FileReader
from model import Sale, ZipCode
from uszipcode import SearchEngine, SimpleZipcode
from shapely.geometry import Point

#graph size
mapSize = (150,150)
mapColor = '#3B3C6E'

# nycData column names converted by Pandas Dataframe
buildingCategoryCol = '_3'
buildingClassPresentCol = '_8'
zipCode = '_11'
buildingClassAtSaleCol = '_19'
salePriceCol = '_20'
saleDateCol = '_21'

WORKING_DIRECTORY = os.getcwd()
CSV_FILE = 'data/rollingsales_queensSample.csv'
NYC_ZIPCODE_GEOJSON = 'data/newyork.zipcode.geojson'


zipCodes = None


def main(args):
    df = FileReader.parseCsvFile(CSV_FILE)
    sales = populateSales(df)
    zipCodes = populateZipcodes(sales, SearchEngine())

    # Create map of new york
    fig, ax = matlibPlot.subplots(1, figsize=mapSize)
    baseMap = generateMapOfNyc(ax)

    zipCodeGeoDataframe = generateSalesInfoDataframe(zipCodes)

    zipCodeGeoDataframe.plot(ax=baseMap, column = 'Price', marker="<", label = 'Price(USD)');
    _ = ax.axis('off')
    matlibPlot.legend()
    matlibPlot.savefig('Test_home_prices.png',bbox_inches='tight');
    breakpoint()

    matlibPlot.show()


    print("End world")

def generateMapOfNyc(mapBase):
    mapOfNyc = geopandas.read_file(NYC_ZIPCODE_GEOJSON)
    baseMap =  mapOfNyc.plot(ax = mapBase, color= mapColor)
    return baseMap


def generateSalesInfoDataframe(zipCodes):
    # data_tuple = list(zip(zipCodes.sales))
    prices, latitudes, longitudes = getListsFromZipcodeData(zipCodes)
    salesInfoDataFrame = {'Price' : prices, 'lat' : latitudes, "long" : longitudes}
    sales_panda_dataFrame = pandas.DataFrame(salesInfoDataFrame)

    #convert lat and long into coordinate point
    sales_panda_dataFrame['coordinates'] = sales_panda_dataFrame[['long','lat']].values.tolist()
    sales_panda_dataFrame['coordinates'] = sales_panda_dataFrame['coordinates'].apply(Point)

    sales_geopanda_dataframe = geopandas.GeoDataFrame(sales_panda_dataFrame, geometry='coordinates')
    return sales_geopanda_dataframe




# returns list of sale price and zipcode, from List<Zipcodes>
def getListsFromZipcodeData(zipCodes):
    prices = []
    latitude = []
    longitude = []

    for zipcode in zipCodes:
        for sale in zipcode.sales:
            prices.append(sale.salePrice)
            latitude.append(zipcode.lat)
            longitude.append(zipcode.long)


    return (prices, latitude, longitude)




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
