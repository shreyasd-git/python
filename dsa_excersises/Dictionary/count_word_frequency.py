#To coout the frequency of words in given list of words

def count_word_freq(words):
    #initialise dictionary
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count

words = ['apple', 'oranges', 'apple', 'orange', 'grape', 'pineapple', 'apple', 'orange']

print(count_word_freq(words))


#Time Complexity - O(n) -> all items in list are traversed once
#Space Complexity - O(n) -> in worst case all elements could be unique and we would be updating/adding all elemnts in dict