# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 21:33:07 2017

@author: abhil
"""

import json
from pprint import pprint

with open('datafile.txt') as data_file:
    data = json.load(data_file)
    
pprint(data)