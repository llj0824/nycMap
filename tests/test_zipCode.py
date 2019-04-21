#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from nycmap.model.ZipCode import ZipCode
from nycmap.model.Sale import Sale
from uszipcode import SimpleZipcode

expectMedian = 9

def getTestZipCode():
  s1 = createTestSaleObj(0,0)
  s2 = createTestSaleObj(9,0)
  s3 = createTestSaleObj(199,0)
  zipCodeInfo = SimpleZipcode()

  testObj = ZipCode(s1, zipCodeInfo)
  testObj.append(s2)
  testObj.append(s3)
  return testObj


def createTestSaleObj(salePrice, zipCode):
  sale = Sale()
  sale.salePrice = salePrice
  sale.zipCode = zipCode
  return sale

def getTestSimpleZipcode(longitude, latitude):
  zipCodeInfo = SimpleZipcode()
  zipCodeInfo.lng = longitude
  zipCodeInfo.lat = latitude
  return zipCodeInfo



def testGetMedianSalePrice():
  testObj = getTestZipCode()
  assert testObj.getMedianSalePrice() == expectMedian


