# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 19:10:56 2020

@author: satwi
"""

#functions

def oper(a,b):
    print("Sum",a+b)
    print("Sub",a-b)
    print("Mul",a*b)
    print("Div",a/b)
    print("Pow",a**b)

oper(20,80)

i=1
j=1
while(i<10):
    print("Oper call")
    oper(i,j)
    i=i+1
    j=j+1

def oper(a,b):
    Sum=a+b
    Sub=a-b
    return(Sum,Sub)

a,b=oper(10,20)
c=oper(10,20)
c
type(c)

def printhello(fname,lname):
    print("Hello",fname," ",lname," Welcome")

printhello("Anne","Teli")
    
def totalsale(x,y):
    return(x+y)

totalsale()
totalsale(20,30)

import random

x=random.radiant(100,100)
x

L1=[11,12,13,14,15,16,17]
random.choice(L1)

import random

l1=[]
l2=[]
l3=[]
l4=[]
i=0
while(i<4):
    l1.append(random.radiant(100,1000))
    l2.append(random.radiant(100,1000))
    l3.append(random.radiant(100,1000))
    l4.append(random.radiant(100,1000))
l1
l2
l3
l4

import random
st="abcdef"
st
random.choice(st)

random.choices(st,k=3)

d1={"name":"Anne","rollno":101,"class":"E"}
type(d1)
random.choices(list(d1),k=3)

s1={1,2,3,4,5}
random.choices(list(s1),k=2)

import random as rd
rd.choices(list(s1),k=2)
rd.randrange(9)

s1={1,2,3,4,5}
l1=list(s1)
l1(2)

random.randint(1,1000)

import random
for i in range(5):
    random.seed(0)
    print(random.randint(1,1000))
    
 for i in range(5):
    random.seed(150)
    print(random.randint(1,1000))   
    
import numpy as np

np.random.randint(100,1000)
np.random.randint(10,1000,size=10)

#similar type of data
#indexed accessible
#mutable
arr=np.random.randint(10,1000,size=10)
arr[1] 
arr[2]=200
arr

arr=np.random.randint(10,1000,size=(5,4))
arr[0,0]
arr[1,4]
arr[1,3]

arr[0,0:3]
arr[:,0:2]
arr[0,0:3]
arr[:,2:4]
arr[2:4,1:3]
arr

arr[-2:-1,:]
arr[-2:,:]
arr[-2:,-2:]

range(0,10,2)

np.arange(10)
np.arange(10,20)
arr1=np.arange(10,20)

arr1.shape
arr1
arr1reshape=arr1.reshape(2,5)
arr1reshape

arr2reshape=arr1.reshape(10)
arr2reshape
arr2reshape.shape

arr3reshape=arr1.reshape(2,5)
arr3reshape
arr3reshape.shape

a=np.zeros((2,4))
a
a=np.ones((2,4))
a
a=np.ones((2,4),dtype='int32')
a

l1=[]
l1.append(2)
l1

arr6.append([2])

arr5=np.empty(1)
arr5.shape
np.eye(4,2)
np.linspace(0,10,num=4,dtype='int32')

























