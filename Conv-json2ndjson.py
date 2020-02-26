# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:00:33 2020

@author: mbacon
"""

import json

with open("stepup.json", "r", encoding="utf8") as read_file:
    data = json.load(read_file)
result = [json.dumps(record) for record in data]
with open('stepupOUT.json', 'w') as obj:
    for i in result:
        obj.write(i+'\n')