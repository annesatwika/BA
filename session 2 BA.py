# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 14:21:36 2020

@author: satwi
"""

#Mutable
#List (is heterogeneous)

L1 = [2,3,4,5,6]
L1[0]
L1[1:4]
L2= [1,"anne",2.3,False,2.66]
L2[3]

#
for key in L2:
    print(key)
    print(i)
    
#Mutable
L2[2]=5.50
L2

L2.count("anne")
len(L2)
L2.append("teli")
L2
L2.remove("anne")
L2
L2.pop()
L2.remove["teli","teli"]

PopValue=L2.pop(1)
PopValue
del L1[0]
L1

L1.clear()
L1

L2= [1,"anne",2.3,False,2.66]
L2
L1 = L2
L1
L2
L1.pop()
L1
L2

L1 = L2.copy()
L1
L2

L1..pop()
L1
L2

Start = 5
End = 100
Jump = 2

a=range(End)
a
list(a)

b=range(Start, End, Jump)
b
list(b)

L3 = [1,2,6,8,5]
L3.sort()
L3

L4=["anne","satwika","teli"]
L4.sort()
L4

L5=L3+L4

L3.pop()
L5

#set

set={1,2,3,4,5}
type(set)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s1.union(s2)
s1.add(6)
s1.add(4)
s1
s1.add("teli")
s1
# add only takes one arguement
s1.update("teli",7)
s1
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s1.update([8,9,10])
s1

s1.discard(21)
s1

s1.pop()
s1.intersection(s2)
s1.difference(s2)

#Dictionary

st={'rollno':1}
st
type(st)

st={'rollno':1,'Name':"anne",'Educ':"MBA"}
st
st['Name']
st.get('Educ')

#keys
for i in st:
    print()
st.values()
#values
for i in st.values():
    print(i)

"MBA" in st.values()

st['Educ']="BTECH"
st

pop_ele=st.pop('Name')
pop_ele

st={'rollno':1,'Name':"anne",'Educ':"MBA"}
for i in st.items():
    print(i)

for i,j in st.items():
    print("key",i)
    print("Value",j)

#Tupple

t1=(1,2,3,4)
t1[0]

for i in t1:
    print(i)

t1=("anne","satwika","teli")

if ("anne" in t1):
    print("hi")

L1=list(t1)
L1
type(t1)
type(L1)













