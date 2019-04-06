import sys
import pandas
import os
from util import FileReader
from model import Area, Sale, ZipCode

# column names converted by Pandas Dataframe
buildingCategoryCol = '_3'
buildingClassPresentCol = '_8'
buildingClassAtSaleCol = '_19'
salePriceCol = '_20'
saleDateCol = '_21'

WORKING_DIRECTORY = os.getcwd()
CSV_FILE = 'data/rollingsales_queensSample.csv'


def main(args):
    df = FileReader.parseCsvFile(CSV_FILE)
    

    # TODO: map each row into sales
    # create Zipcode containing sales
    # create area containing multiple zipcode
    sales = populateSales(df)

    # Todo: group sales by Zipcode
    for s in sales:
        s.print()

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
        sales.append(sale)

    return sales;


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main(sys.argv[:])
