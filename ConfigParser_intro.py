# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 13:05:47 2016

@author: AYUSH
"""
# importing ConfigParser
import ConfigParser

# creating instance of ConfigParser.RawConfigParser
config = ConfigParser.RawConfigParser()
print config

config.read("config.cfg")

print config.get('classifier','port')
