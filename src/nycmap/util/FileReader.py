import pandas
import os

def parseCsvFile(filePath):
    df = pandas.read_csv(filePath)
    return df


def parseExcelFile():
    filePath = '../../data/rollingsales_queens.xls'
    df = pandas.read_excel(filePath, skiprows=4)
    return df


# def getColumnNames():
#     return (salePrice, saleDate, buildingCategory, buildingClassPresent, buildingClassAtSale)
