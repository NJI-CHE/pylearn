#write a function that returns the maximum of  three numbers
def max_of_two(x,y):
    #Check if x greater than y
    if x > y:
        return x
    return y

def max_of_three(x,y,z):
    #Call max_of_two functions and then compare to find the max
    return max_of_two(x, max_of_two(y,z))

#print the result by calling max_of_three
print(max_of_three(1,2,3))