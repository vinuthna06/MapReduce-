#!/usr/bin/env python3

import sys
import csv 

csvreader = csv.reader(sys.stdin)



for row in csvreader:

    asin = row[2]
    prediction_result = row[len(row)-1]
    prediction_result= prediction_result.strip().replace(" ", "_")
    print(asin +"-"+prediction_result + '\t' + '1')

