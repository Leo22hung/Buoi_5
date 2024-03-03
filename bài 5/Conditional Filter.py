def filter_dict(dictionary, condition):
    filtered_dict = {key: value for key, value in dictionary.items() if condition(key, value)}
    return filtered_dict

# Example usage:
def is_even(key, value):
    return value % 2 == 0

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_result = filter_dict(my_dict, is_even)
print("Filtered dictionary:", filtered_result)
