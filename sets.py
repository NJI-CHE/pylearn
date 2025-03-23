#A set is a collection which is unordered, unchangeable and unindexed
thisset = {"apples", "pears", "mango", "kiwi", "mango", True, 1, False, 0}
print(thisset)
print(len(thisset))

## Set() Constructor
movies = ("The A-team", "Predator", "Kunfu Hustel", "Predator")
moviesset = set(movies)


for x in thisset:
    print(x)


#adding elements to a set
moviesset.add("Terminator")
#print(moviesset)

#adding two sets
thisset.update(moviesset)
#print(thisset)

##Removing set items
thisset.remove(False)
#print(thisset)

set1 ={1,2,3,4,5}
set2 = {4,5,6,7,8}

set3 = set1.union(set2)
print(set3)

set4 = set1.intersection(set2)
print(set4)