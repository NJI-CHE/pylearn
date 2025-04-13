#List are used to store multiple items in a single variable
#List are created using sqaure brackets
##propeties of list ; odered, changeable and they allow duplicate  values
x = []
y = 3
z= 2.0

list1 = ["apple", "mangoes", "berries"]
list2 = [1,2,3,4,5,5, 6, 7,7,7]
list3 = ['abc', 34, True, 40, "male"]
#print(myList)
#print(myList1[0])


##list methods
##Methods are inbuilt functions 
# we can use to perform particular task
print(len(list1))

#type method
print(type(z))

#Accessing items
print(list1[-2])


#Range of Indexes
print(list2[2:5])
print(list3[:4])

#Check if item exists
if 40 in list3:
    print("Yes, '40 is in list3")

#Change item value
list1[0] = 'Dragon fruit'
#print(list1)

##Change multiple item values
list3[1:2] = ["Nji", "Diego"]
#print(list3) 


#insert items
list1.insert(3, 'watermelon')
#print(list1)


##Exercise
#Append 2 elemest to list 2 and 3 at index 1

#Extend list
list1.extend(list2)
#print(list1)

##Remove List elements
list1.remove('berries')


#remove specifird index
list1.pop(5)
#print(list1)

#Clear the list
#clear() emmpties the list

list2.clear()
#print(list2)
#help

#loops list
#for p in list1:
    #print(p)


list4 = ['Messi', "Ronaldo", "Fernades", "Etoo"]
#for i in range(len(list4)):
    #print(list4[i])


#Using a while loop to go through a List
#i = 0
#while i < len(list4):
    #print(list4[i])
    #i = i+1

#Looping using List Comprehension
#[print(x) for x in list4]

##sorting list aphanumerically
list4.sort()
print(list4)

list5 = [2, 45, 100, 30, 10, 4, 7]
list5.sort(reverse=True)
print(list5)

combineList = list1 + list4
print(combineList)