import sys
import pandas
import os
from util import FileReader
from model import Area, Sale, ZipCode


salePriceCol = 'SALE PRICE'
saleDateCol = 'SALE DATE'
buildingCategoryCol = 'BUILDING CLASS CATEGORY'
buildingClassPresentCol ='BUILDING CLASS AT PRESENT'
buildingClassAtSaleCol = 'BUILDING CLASS AT TIME OF SALE'


WORKING_DIRECTORY = os.getcwd()
CSV_FILE = 'data/rollingsales_queensSample.csv'

def main(args):
    df = FileReader.parseCsvFile(CSV_FILE)
    
    # TODO: map each row into sales
    # create Zipcode containing sales
    # create area containing multiple zipcode
    populateSales(df)
    
    print("End world")


def populateSales(dataFrame):
    sales = []
    # [salePrice, saleDate, buildingCategory, buildingClassPresent, buildingClassAtSale]
    for tup in dataFrame.itertuples():
        row = dict(tup)
        sale = Sale(row[salePriceCol], row[saleDateCol],
                    row[buildingCategoryCol], row[buildingClassPresentCol],
                    row[buildingClassAtSaleCol])
        print(sale)
        sales.append(sale)
        break
        

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main(sys.argv[:])

