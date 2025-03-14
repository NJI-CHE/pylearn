def shortest_longest_words(words_list):
    shortest_word = min(words_list, key=len)
    longest_word = min(words_list, key=len)
    return shortest_word, longest_word

words = ['mango', 'pear', 'palm', 'guava','sugarcane']
result = shortest_longest_words(words)

print(result)
