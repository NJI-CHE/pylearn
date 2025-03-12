#String inpython are surrounded by either '' or ""
x = 'hello1'
x = "hello"
#print(x)

a = """ My name is Nji
and I am a python tutor"""

#print("Programming is fun")


##Strings are arrays
b = "Hello World"
#print(b[0])

##Looping through a string
#for z in 'South America':
    #print(z)

##String Length
#print(len(b))

##Check string: checks if a certain chraracter or phrase is present
txt = "The best things in life are free!"
#print("2" in txt)

#Slicing:: retuns a rangge of chracters
#Specify the start and the end index
c = "Coding is fun"
print(c[2:5])
print(c[2:])
#Negative Indexing; starts the slice from the end of the string
print(c[-5:-1])

#replace: Method that replaces a string with another string
print(c.replace("C", "K"))

#Split Strinng: returns a list where the text between 
#specifies separator becomes the list items
d = 'We have classes, at 12:30 am WAT'
print(d.split("t"))

#String Concatenation: This means combining 2 string using + operator
e = "Hello"
f = "world"

g = e + " " + f
print(g)

