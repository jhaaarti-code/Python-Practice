# print ("Hello world")
# print("namastey youtube we are learning python")
# #comments
# #hello i am aarti how are you
# """hello this is multiline
# aarti
# jha
# carmel"""
# #variable
# sher = "harsh bhaiya"
# a = 12
# #naming convention
# SheryiansSchool = "students" #pascal case
# sheryiansSchool = "students" #camel case
# sheriyans_school = "students" #snake case

# #integer
# a = 12
# print(type (a))
# #float
# b = 56.8
# c = 12/3

# print(type(b))
# print (type(c))
# #if number is in decimal or in the form of p/q then it will be float

# #complex
# v = 24j
# print (type(v))

# #tring
# #anything that are available in our keyboard is called string

# st = '123445566765 dsgsrehddtdf &*5/#@!$'
# print (type(st))

# #boolean

# #data type which will and always give the result true and false

# b = True

# a = False

# print(type(b))
# print(type(a))

# """String"""

# a = "A"
# print(ord(a))

# a = 65
# print (chr(a))

# #string indexing
# a = "SHER"
# print(a[1])
# print(a[1],a[-3])

# #string slicing

# a = "SHER CODER"
# print(a[0:4:1])
# print(a[5::1])

# #type conversion
# a = 12
# a = str(a)
# print(type(a))

# a = 12
# a = int (a)
# print(type(a))

# a = 10
# print(bool(a))

# a = "Hello"
# print(bool(a))

# a = 0
# print(bool(a))

# #implicit
# a = 12
# print(a/4)

# name = "Aarti"
# age = "20"
# print(name,age)
# print("hello my name is", name , "and my age is", age )
# #or
# print(f"my name is{name} and my age is {age}")
# #input
# #name = input("what is your name")
# #print(name)
# #print(type(name))

#  # accept number from a user

# #number = input ("give me a number")
# #print(number)

# # accept age from the user and print it

# #age = input("give me an age")
# #print (age)

# # operators

# a = 12
# b = 20
# print(a+b)
# print(b-a)
# print(a*b)

# a = 5
# b = 20
# print(b/a)
# print(b//a) # floor value

# a = 5
# b = 32
# print(b/a)
# print(b//a)

# # exponential
# print(5**2)

# #modulo
# print(32%5)

# # python follows BODMAS rule

# # assignment operators

# #a = 12
 
#  # compound asignment operations
 
# t = 20

# t = t + 20

# t = t + 40
# print (t)

# # or

# t = 20

# t += 20

# t += 40
# print(t)
# # a-=
# # a*=
# # a/=
# # a//=
# # a**=

# # comparison operators

# a = 12
# b = 12

# print(a==b)

# print(a!=b)

# print(a>b)

# print(a<b)

# print(45<67)

# print(23>=23)

# print(45<=45)

# # Unicode

# print(ord("A"))
# print(ord("a"))

# print("A">"B")
# print("ABC" > "BCD")

# # you cannot compare a string with an integer

# # 3 types of logical operators 
# # 1. and - return true if both condition is true
# # 2. or - return true if atleast one condition is true
# # 3. not - reverse the boolean value

# # and

# print (123>100 , 34==34)
# print (123>100 and 34==34)
# print (123>100 and 34==34 and 45<90)
# print (123>100 and 34==34 and 45<90 and 12>90)

# # or

# print (12!=12 or 23==45 or 67==56 or 10>5)
# print (12==12)
# print (not 12==12)

# 1.print (126>130)
# 2.print ((456==456) != (235==236))
# 3.print(12<10 or 45==56 or 69>70 or 15!=13)
# 4.print(True and bool(0))

# IF else

# a = 13
# if a > 10:
#     print("I will do task A")
    
# else:
#     print("I will do task B")

# a = 6
# if a > 10:
#     print("I will do task A")
    
# else:
#     print("I will do task B")

# money = int(input("please provide me the money -: "))

# if money == 10:
#     print("I will have a choco bar icecream")
    
# else:
#     print("I will have a mango dolly icecream")

# money = int(input("please provide me the money -: "))

# if money == 10:
#     print("I will have a choco bar icecream")
    
# elif money == 20:
#     print("I will have a mango dolly icecream")
    
# elif money == 30:
#     print("I will have a frosty")
    
# else:
#     print("I will have a cone icecream")

# num1 = int(input("please tell your first number"))
# num2 = int(input("please tell your second number"))

# if(num1 > num2 ):
#     print(num1)
    
# else:
#     print(num2)

# gen = input("please tell your gender as character(M or F) -:")
# if gen == 'M'or gen == m:
#     print("GOOD MORNING SIR")
    
# else:
#     print("GOOD MORNING MAM")

# or

# gen = input("please tell your gender as character(M or F) -:")
# if gen == 'M'or gen == 'm':
#     print("GOOD MORNING SIR")
    
# elif gen == 'F' or gen == 'f':
#     (print("GOOD MORNING MAM"))
    
# else:
#     print("unidentified gender")
    
# number = int(input("give me a number"))
# if number % 2 == 0:
#     print("NUMBER IS EVEN")
    
# else:
#     print("NUMBER IS ODD")


# name = (input("please tell your name"))
# age = int(input("tell your age"))
# if(age > 18):
#     print(f"hello{name} you are a valid voter")
    
# else:
#     print(f"hello{name} you are not a valid voter")

# year = int(input("tell your year"))

# if year % 100 == 0 and year % 400 == 0:
#     print("Its a leap year")
    
# elif year % 100 != 0 and year % 4 == 0:
#     print("Its a leap year")

    
# else:
#     print("not a leap year")

# t = int(input("please tell the temperature"))

# if t < 0:
#     print("Freezing cold")
    
# elif t >= 0 and t < 10:
#     print("Very cold")
    
# elif t >= 10 and t < 20:
#     print("Cold")
    
# elif t >= 20 and t < 30:
#     print("Pleasant")
    
# elif t >= 30 and t < 40:
#     print("Hot")
    
# else:
#     print("Very Hot")

# For loop
#range(s,s,s) s - start , s - stop , s - step

# For loop

# a = range (1,21,1)
# for i in a:
#     print(i)
    
#     # or
    
# for i in range (1,21,1):
#     print(i)
    
#     # or
    
# for i in range (21):
#     print(i)
    
# 20 - 50

# for i in range (20,51,1):
#     print(i)
    
# # 16 - 1

# for i in range (16,0,-1):
#     print(i)
    
# # -5 - -15

# for i in range (-5,-16,-1):
#     print(i)
    
# # lets print a table of 5

# for i in range (5,51,5):
#     print(i)
    
# # lets print a table of 7

# for i in range (7,71,7):
#     print(i)
    
# n = int(input("which table you want ? "))

# for i in range (n, (n*10)+1, n):
#     print(i)

# a = "AARTI"
# for i in range(0,5,1):
#     print(a[i])
    
# a = "HELLO MY NAME IS AARTI JHA"
# print(len(a))
# for i in range (0,26,1):
#     print(a[i])

#  #or

# a = "HELLO MY NAME IS AARTI JHA"
# print(len(a))
# for i in range (len(a)):
#     print(a[i])

# a = "AARTI"
# for i in a:
#     print(i)

# break

# for i in range (1,21,1):
#     if(i==15):
#         break
#     else:
#         print(i)

# for i in range (1,21,1):
#     if(i==15):
#         continue
#     print(i)

# for i in range (1,21,1):
#     if i == 15:
#         print("break statement is executed")
#         break
#     print(i)
    
# else:
#     print("break staement is not executed")
       
# for i in range (1,21,1):
#     if i == 56:
#         print("break statement is executed")
#         break
#     print(i)
    
# else:
#     print("break staement is not executed")

 # break - run , else - will not run
 # break - will not run , else - will run
 
 # loop questions
 
# n = int(input("please tell you number"))

# for i in range(n):
#     print("HELLO WORLD")

# n = int(input("please tell your number"))
# for i in range(1,n+1,1):
#     print(i)

# n = int(input("please tell your number"))
# for i in range(n,0,-1):
#     print(i)

# n = int(input("which table you want"))
# for i in range(n,(n*10)+1,n):
#     print(i)

#  or

# n = int(input("which table you want"))

# for i in range (1,11,1):
#     print(f"{n} * {i} = {n*i}")

# n = int(input("pleae tell your number"))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(sum)
    
# n = int(input("please tell your number"))

# fact = 1

# for i in range(1,n+1):
#     fact = fact*i
    
    
# print(f"your factorial is {fact}")




       

    





