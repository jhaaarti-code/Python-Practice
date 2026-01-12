# Data structures - storing multiple values in one variable
# 4 types of in build data structures
# List
# Tuple
# Dictionary
# Set

# Lists powers -:
# Mutable - object's value can be changed after creation
# Duplicates - means same value occuring multiple times. Lists allows this
# Ordered - This means you can access elements using their position(index)
# Hetrogeneous - Lists have heterogeneous nature that means we can have multiple data type inside the list

# List syntax - we have to use square bracket

# a = [12,13,14,16,19,34.5,True,print()]

# List indexing
#print(a[0])
# print(a[1])

# List slicing
# print(a[0:5:1])
# print(a[-2])

# List Traversing

# 1st way using index

# for i in range (len(a)):
#     print(a[i])

# 2nd way directly on values

# for i in a:
#     print(i)

# List methods

# print(dir(list))

# help(list)

# l = [1,2,3,4,5]

# l.append(6)
# l.append(7)

# print(l)

# l = [1,3,4,5]

# l.insert(1,2)

# print(l)

# l = [1,3,4,5]

# l.extend([8,10,15])

# print(l)

# l = [1,2,3,4,5]
# l.remove(2)
# print(l)

# l = [1,2,3,2,4,5]
# l.remove(2)
# print(l)

# l = [1,2,3,4,5]
# l[0] = 10
# print(l)

# Some questions on list

# print positive and negative elements of an list

# l = [-45,67,12,-68,-69,34]

# print("positive elements are")

# for i in l:
#     if i >= 0:
#         print(i)
# print("negative elements are")
        
# for i in l:
#     if i <0:
#         print(i)

# Mean of list elements

# l = [12,435,67,89,23,25,69]

# sum = 0

# for i in l:
#     sum = sum + i
    
# print (sum/len(l))

# Find the greatest element and print its index too

# l = [12,567,43,235,347,568,45,7]

# largest = l[0]
# index = 0

# for i in range (len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i
        
# print (f"your largest number is {largest} at index {index}")

#  Find the second greatest element

# l = [12,16,13,19]

# largest = l[0]
# sec_largest = l[0]

# for i in l:
#     if i > largest:
#         sc_largest = largest
#         largest = i
        
# print (largest , sec_largest)

# l = [12,16,13,19,17]

# largest = l[0]
# sec_largest = l[0]

# for i in l:
#     if i > largest:
#         sc_largest = largest
#         largest = i
        
#     elif i > sec_largest:
#         sec_largest = i
        
# print (largest , sec_largest)

#  Check if list is sorted or not

# a = [16,13,14,15,16]

# for i in range (len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break
    
# else:
#     print("your list is sorted")

# a = [12,13,14,15,16]

# for i in range (len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break
    
# else:
#     print("your list is sorted")

# tuple

# a = (1,2,3,4,5,5,5.5,print(),"hello")

# print(type(a))

# tuple powers -:
# immutable - you cannot change the values of tuple
# dublicates - you can have duplicate values in tuple there are no restriction
# ordered - set are ordered and you can access them through index values
# Heterogeneous - set also have heterogeneous nature and can have different type of data structure in tuple

# print(a[0])
# print(a[1])

# for i in a:
#     print(i)

# for i in range(len(a)):
#     print(a[i])

# methods of tuple

# index = a.index(5)
# print(index)

# count = a.count(5)

# print (count)

# tuple unpacking

# a,b,c,d = (1,2,3,4)
# print(a)
# print(b)
# print(c)
# print(d)

# a = (1)
# print(type(a))

# a = (1,)
# print(type(a))

# Set

# s = {1,2,3,4,5,5,4}

# sets powers -:

# mutable - sets are mutable you cn change the values of set
# duplicates - you cannot have any duplicate values in set
# unordered - sets are unordered and you cannot access them through index values
# Heterogeneous - set is semi heterogeneous itcan store some data type like string, numbers , tuples but not everything

# print(s)

# b = hash("Hello")
# print(b)

# c = hash((1,2,344))
# print(c)

# set traversing

# a = {1,2,3,4,5}
# for i in a:
#     print(i)

# a = {1,8,9,2,3,4,5}
# for i in a:
#     print(i)

# set methods

# a = {1,2,3,4}

# a.pop()
# print(a)

# a = {1,2,3,4}

# a.clear()
# print(a)

# union set

# a = {1,2,3,4,5}
# b = {4,5,6,7,8}

# s = a.union(b)
# print(s)

# or

# a = {1,2,3,4,5}
# b = {4,5,6,7,8}

# s = a|b
# print(s)

# intersection set

# a = {1,2,3,4,5}
# b = {4,5,6,7,8}

# s = a.intersection(b)
# print(s)

# or

# a = {1,2,3,4,5}
# b = {4,5,6,7,8}

# s = a&b
# print(s)

# a = {1,2,3,4,5}
# b = {4,5,6,7,8}

# s = a.difference(b)
# print(s)

# a = {1,2,3,4,5}
# b = {4,5,6,7,8}

# s = b.difference(a)
# print(s)

# or

# a = {1,2,3,4,5}
# b = {4,5,6,7,8}

# s = b-a
# print(s)

# symmetric difference

# a = {1,2,3,4,5}
# b = {4,5,6,7,8}

# s = b^a
# print(s)

# or

# a = {1,2,3,4,5}
# b = {4,5,6,7,8}

# b -= a
# print(b)

#  in set value is stored in hashing form

# Dictionary

# Dictionary powers -:

# Mutable - Dictionaries are mutable , meaning you can change , add or remove key value pairs after creation
# Duplicates - keys must be unique , but you can have duplicate in values
# order - dictionary follows insertion order
# Hetrogeneous - a dictionary can store different type of keys and values like integers, strings, lists or even another dictionary

# d = {} 
# print(type(d))

# d = {1,2} 
# print(type(d))

# d = {1:"hello", 2:56} 
# print(type(d))

# my dictionary keys are kind of index values

# CRUD

# d = {10:100,20:200,30:300,40:400,50:500}
# print(d[10])

# d = {10:100,20:200,30:300,40:400,50:500}
# d[10] = 1000
# print(d)

# d = {10:100,20:200,30:300,40:400,50:500}
# d.update({50:500})
# print(d)

# d = {10:100,20:200,30:300,40:400,50:500}
# d[50] = 500
# print(d)

# d = {10:100,20:200,30:300,40:400,50:500}
# del d[30]
# print(d)

#dictionary traversing

# d = {10:100,20:200,30:300,40:400,50:500}

# for i in d:
#     print(i)

# d = {10:100,20:200,30:300,40:400,50:500}

# for i in d:
#     print(d[i])

# or

# d = {10:100,20:200,30:300,40:400,50:500}

# for i in d.values():
#     print(i)

# dictionary methods

# help(dict)

# d = {10:100,20:200,30:300,40:400}
# d.clear()

# a = [1,2,3,4,5]

# b = a

# b[0] = 100

# print(a)

# a = [1,2,3,4,5]

# b = a.copy() shallow copy

# b[0] = 100

# print(a)

# a = [1,2,3,4,5]

# b = a.copy()

# b[0] = 100

# print(b)

# d = {10:100,20:200,30:300,40:400}

# d2 = d.copy()

# d = {10:100,20:200,30:300,40:400}
# d2 = d.get(20)

# d = {10:100,20:200,30:300,40:400}
# print(d.items())

# Dictionary questions

# write a python script to merge two python dictionaries

# d1 = {10:100,20:200,30:300}
# d2 = {40:400,50:500,60:600}

# for i in d2:
#     d1[i] = d2[i]
    
# print(d1)

# write a python program to sum all the values in a dictionary

# d1 = {10:100,20:200,30:300}
# sum = 0

# for i in d1:
#     sum = sum + d1[i]
    
# print(sum)

# 

# a = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,7,8]

# d = {}

# for i in a :
#     if i in d.keys():
#         d[i] += 1
        
#     else:
#         d[i] = 1
        
# print(d)

# or

# a = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,7,8]

# d = {}

# for i in a :
#     if i in d:
#         d[i] += 1
        
#     else:
#         d[i] = 1
        
# print(d)

# 

# d1 = {10:100,20:200,40:300}
# d2 = {40:400,50:500,60:600}

# for i in d2:
#     if i in d1.keys():
#         d1[i] += d2[i]
        
#     else:
#         d1[i] = d2[i]
        
# print(d1)



        
     























        



