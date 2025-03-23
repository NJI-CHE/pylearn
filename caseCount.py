#Program hat counts the number of uppercas eand lowercase letter in a string
#Input is a string
#Process the string to get upper and lowercase letters
# To do this, we use the isupper and islower inbuilt methods
#The increment for values of upper and lowercase respecively.

#Step 1 " Write a function that counts the number of upper and lower case xters in
# a string called s"

def stringTest(s):
    #We create a dictionary to store the counts of upper and lower case
    d={"UPPER_CASE": 0, "LOWER_CASE": 0}

    #Itereate through each character "c" is in upper case
    for c in s:
        #check if character 'c' is upper case
        if c.isupper():
            d["UPPER_CASE"] += 1
        
        #check id 'c' is lower case
        elif c.islower():
            d["LOWER_CASE"] += 1
        else:
            #if 'c' in neither lower nor upper
            pass

    #print the given statement
    print('Original String: ', s)

    #print the number of upper case
    print("Number of upper case character: ",d["UPPER_CASE"])

    print("Number of lowercase characters: ", d["LOWER_CASE"])

#Call the stringTest function and pass the input string
stringTest("Hello I am Nji and I love o Code in Python")
