# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 16:55:41 2016

@author: AY355513
"""

print "\n-----Numpy tuils Part-1------\n"
# importing numpy as np
import numpy as np
# creating array by inserting element one by one
a0 = np.array([1,2,3,4])
# creating a python list
p1 = [23,23,34.5,45.6,45,67]
# creating a numpy array from python list
a1 = np.array(p1)
# print array values and type
print "\n###One by One element####"
print a1
print type(a1) # finding type of a1
print a1.ndim # returns number of rows
print a1.shape # returns shape of matrix if
print len(a1) # return  number of columns
# functions for creating arrays
print "\n###Evenly spread array###"
a2 = np.arange(10) # creating evenly spread array from 0 to 9
print "using arange with evenly spread"
print a2
a3 = np.arange(1,11,2) # arange syntex for start end(exculisive) and step
print "using arange with start and end and step syntex"
print a3
a4 = np.arange(1,18,2).reshape(3,3)
print "using arange with reshape"
print a4
print "\n###Creating array based on number of points###"
a5 = np.linspace(0,3,10) # start , end and number of points
print "using linspace"
print a5
print a5.shape
a6 = np.linspace(0,1,6).reshape(3,2)
print "using linspace and reshape"
print a6
print "\n###Common arrays###"
a7 = np.ones((4,6)) #creating a 4*6 array of ones
print "using ones"
print a7
a8 = np.zeros((2,3)) # creating zero matrix of shape 2*3
print "using zeros"
print a8
a9 = np.eye(3) # creating daignol matrix with values 1
print "using eye"
print a9
a10 = np.diag(np.array([11,22,33]))
print "using diagnol with array"
print a10
print "\n###Random numbers###"
print "Using random seed function"
np.random.seed(1234)
a11 = np.random.rand(4) #uniform distribution
print "using random.rand"
print a11
a12 = np.random.randn(6).reshape(2,3) #gaussian disytributiom
print "using random.randn"
print a12
print "\n###Understanding dtypes"
print a0.dtype
print a1.dtype
print "using dtype explicitly"
a13 = np.array([1,2,3,4],dtype="float")
print a13
print a13.dtype
print a9.dtype # by default dtype is float

print "\n-----Numpy tuils Part-2------\n"
print "\n###Array indexing###"
a14 = np.arange(10)
print a14[0], a14[3] #indexing in python begin with 0
print "python idiom for reversing array"
a15 = a14[::-1] # check python list indexing syntax
print a15
a16 = np.arange(16).reshape(4,4) 
print "Accessing multidimensional array index start from zero"
print a16[0,1],a16[0,0],a16[2]
print a16
print "\n###Array slicing"
print a14[1:] #slicing starting from 1 index to last
print a14[2:4:2] #start at 2 index till 4 index excluding 4 with step of 2
print a16[2:3,1:3] # same rule applies for multi dimensional array
print "\n###Copy and Views###"
b = a0[1:3] #slicing returns view meaningview will share same memory
print "using may share memory"
print np.may_share_memory(b,a0)
b[1]=10
print "update b will result in updation of a10"
print a0
c = a0.copy()
print "copy will not share memory and will make different variable"
print np.may_share_memory(c,a0)
c[2] = 22
print "updating c will not result in updation of a0"
print a0
print "\n###Fancy indexing###" #itislike which function in R
a17 = np.random.random_integers(0,20, 10 )
mask = a17%4 ==0
print "using concept of mask"
print mask
print a17[mask]
print "fency indexing always creates copies and not views"
print np.may_share_memory(a17,a17[mask])




