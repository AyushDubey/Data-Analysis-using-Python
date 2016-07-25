# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 14:27:38 2016

@author: AYUSH
"""

import json
import string
json_string = '{"Name":"Ayush","Rank":22}'
print json_string

# parsing json string
parsed_json = json.loads(json_string)
print parsed_json

print parsed_json['Rank']
print type(parsed_json['Rank'])

print parsed_json['Name']
print type(parsed_json['Name'])
print string.upper(parsed_json["Name"])
rank = 22
print json.dumps({"I am Data":"hi","rank":rank})