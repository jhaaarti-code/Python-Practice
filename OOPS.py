# imperative approach-:

# a = 12
# b = 12
# print(a+b)
# c
# d

# functional approach-:

# def addition(a,b):
#     print(a+b)
    
# addition(12,12)
# addition(56,89)

# sybntax of OOPS

# class First:
#     x = 50
# obj = First()
# print(obj.x)

# classes in oops

# attributes -: variables deined inside class are attributes
# methods -: functions defined inside class are methods
# class Factory:
#     a = 12 #attribute
  
     
#     def hello(self): #method
#          print("how are you") 
         
# # print("hello how are you i am getting initialized")

# print(Factory().a) # access attributes

# Factory().hello() # calling methods

# obj = Factory()

# print(obj.a)
# obj.hello()

# class Faculty:
#     def putdata(self): #method 1
#         self.id = int(input("enter faculty id"))
#         self.name = input("enter name")
#         self.salary = float(input("enter faculty salary"))
        
#     def display(self): #method 2
#         print("faculty id : " , self.id)
#         print("faculty name : " , self.name)
#         print("faculty salary : " , self.salary)
        
# a = Faculty()
# a.putdata()
# a.display()

# class Student:
#     def __init__(self,my_roll, my_name,my_marks):
#         self.rollno = my_roll
#         self.name = my_name
#         self.salary = my_salary
        
#     def average(self):
#         return sum(self.marks)/len(self.marks)
    
#     first_student = student(1,'varun',50,60,70,80,90)
#     print(first_student.name)
#     print(first_student.)

# class Factory:
#     def __init__ (self,material, zips, pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets
        
# reebok = Factory ("leather" , 3, 2)
# campus = Factory ("nylon", 3, 3)

# print(reebok.pockets)
# print(campus.pockets)

# or

# class Factory:
#     def __init__ (self,material, zips, pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets
        
#     def show (self):
#         print(f"your object details are {self.material} , {self.zips} , {self.pockets}")
        
# reebok = Factory ("leather" , 3, 2)
# campus = Factory ("nylon", 3, 3)

# reebok.show()

# types of attributs

# class Animal:
#     name = "lion" # class attribute
    
#     def __init__(self,age):
#         self.age = age # instance attribute
        
#     def show(self):
#         print(f"how are you your age is {self.age}")
        
#     @classmethod #class method
#     def hello (cls):
#         print("how are you brother")
    
    
#     @staticmethod
#     def static ():
#          print("how are you")
   
    


# obj = Animal(12)

# obj.show()
# obj.hello()
# obj.static()

# inheritance

# class Factorymumbai:  #parent class / super class
#     a = "i am an attribute mentioned inside factory"
#     def hello(self):
#         print("hello i am a method mentioned inside factory")
        
# class Factorypune(Factorymumbai): #child class / sub class
#     pass

# obj = Factorymumbai()
# print(obj.a)

# obj2 = Factorypune()
# obj2.hello()

#constructor in inheritance

# class Animal:
#     def __init__(self,name):
#         self.name = name
        
#     def show(self):
#         print(f"hello your name is {self.name}")
        
# class Human (Animal):
#     pass

# animal1 = Animal("lion")
# human1 = Human("Aarti")

# human1.show()
# class Animal:
#     def __init__(self,name):
#         self.name = name
        
#     def show(self):
#         print(f"hello your name is {self.name}")
        
# class Human (Animal):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age
        
#     def show(self):
#         print(f"hello your name is {self.name}  {self.age}")

# animal1 = Animal("lion")
# person1 = Human("Aarti",20)

# person1.show()

# multiple inheritance

# class Animal:
#     name1 = "lion"
    
# class Human:
#     name2 = "Aarti"
    
# class Robots(Animal,Human):
#     name3 = "charli123"
    
# obj = Robots

# print(obj.name1)
# print(obj.name2)
# print(obj.name3)

# class Animal:
#     def __init__ (self,name):
#         pass
    
    
# class Human:
#     def __init__ (self,name,age)
    
    
# class Robots(Human,Animal):
#     name3 = "charli123"
    
# obj = Robots

# multilevel inheritance

# class Factory:
#     def __init__(self,material,zips):
#         self.material = material
#         self.zips = zips
        
# class BhopalFactory:
#     def __init__(self,material,zipsc,colour):
#         super().__init__(material,zips)
#         self.colour = colour
        
# class PuneFactory:
#     def __init__(self,material,zipsc,colour,pockets):
#         super().__init__(material,zips,colour)
#         self.pockets = pockets
    












        
        





