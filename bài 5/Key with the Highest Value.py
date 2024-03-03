def key_with_highest_value(dictionary):
    if not dictionary:  # Check if the dictionary is empty
        return None
    
    max_value = max(dictionary.values())  # Find the maximum value in the dictionary
    for key, value in dictionary.items():
        if value == max_value:
            return key

# Example usage:
my_dict = {'a': 5, 'b': 9, 'c': 2}
result = key_with_highest_value(my_dict)
print("Key with the highest value:", result)
