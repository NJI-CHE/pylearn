## Xtics: Odered and unchangeable
mytuple = ('Manchester United', "Real madrid", "Barca", "Arsenal")
b= ()
a = []

#print(type(b))
#print(type(a))

if "Manchester United" in mytuple:
    print("yes, 'Manchester United' is in mytuple")


tuple1 = ("a", "b", "c", "b", "d")
tuple2 = (1,2,3,3,3,4,5)

tuple3= tuple1 + tuple2
print(tuple3)

x = tuple2.count(2)
print(x)

y = tuple1.index("b")
print(y)

