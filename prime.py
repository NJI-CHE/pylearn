# Write a python functin that check if a number is prime
#Exemple de nombre premier 2,3,5,7....
# Un nombre premier c'est un mumbre qui n'est pas divisible par 2
# n / 2 != 0

#Define a function callled testPrime
def testPrime(n):
    #Check id n is equal to 1
    if (n==1):
        return False
    #check if n is equal to 2
    elif (n==2):
        #if n is 2, return True(2 is a prime number)
        return True
    else:
        #Go through number from 2 to (n-1) using x as iterator
        for x in range (2,n):
            #check if n is divible by x without any remainder
            if (n % x == 0):
                #If it is completely divisible, themn it is not prime so false
                return False
        #if n is not divisible by any number fro 2 to (n-1)
        return True
    
#Call function and test
print(testPrime(11))
            


