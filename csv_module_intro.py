# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 12:25:00 2016

@author: AY355513
"""
# importing csv module 
import csv
with open("csv_test_file.csv",'rb') as f:
    reader = csv.reader(f)
    header = reader.next()
    row_1 = reader.next()
    for row in reader:
        print row
        print row[1]
f.close()
print header
print row_1
