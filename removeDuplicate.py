def removeDuplicates(inputList):
    sortedList = sorted(set(inputList))
    return sortedList

inputList = ['mangoes', 'guava', 'kiwi', 'pear', 'pear', 'futu']
result = removeDuplicates(inputList)

print(result)
