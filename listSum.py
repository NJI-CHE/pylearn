#Define a function named sum that takes a list of numbers
def sum(numbers):
    #Initialise a varible total to store sum of numbers
    total = 0

    #Iterate through each element x in numbers list
    for x in numbers:
        total = total + x
    
    return total

print(sum((7,6,10,23,34,5,6,67,7)))

