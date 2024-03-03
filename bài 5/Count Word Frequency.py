def word_frequency(words):
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

# Example usage:
word_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(word_frequency(word_list))
