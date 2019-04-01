#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from nycmap.util import FileReader

TEST_CSV_FILE = 'data/rollingsales_queensSample.csv'
TEST_COLUMN = "NEIGHBORHOOD"

def testParseExcelFile_correctSize():
    df = FileReader.parseCsvFile(TEST_CSV_FILE)
    assert df[TEST_COLUMN].size == 60
