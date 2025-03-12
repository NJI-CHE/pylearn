#This referes to the various ways in which data is stored
#we have several in built data types in python and the include:
#str, int,float, complex, list, tuple, range, dict, sets, bool, bytes


#type is an inbuilt function that is used to know the datatype of a varible
#Declaring an interger
x = int(5);
print(type(x))

#Declaring a float
y = float(5.0)
print(type(y))


#declaring a string which stores text
intro = "My name is Nji"
name = "Nji Cornelius"
print(type(intro))

#Declaring a list
fruits = ["Apple", "Banana", "Cherry", "Manges"]
a = [10,8, 15, 7, 6]
print(type(fruits))

#Tuples
x = ("nji", "Diego", "Peter", "Jones")
print(type(x))

#dictionary
#mapped datatype, as it stores data in value-pairs
nameAge = {"name":"Nji", "age":28,}
print(type(nameAge))

#set
set = {"cars", "shoes", "houses"}
print(type(set))


#Boolean values
c = True
print(type(c))