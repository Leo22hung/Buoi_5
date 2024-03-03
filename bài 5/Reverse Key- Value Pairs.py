def reverse_dict(dictionary):
    reversed_dict = {value: key for key, value in dictionary.items()}
    return reversed_dict

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_result = reverse_dict(my_dict)
print("Reversed dictionary:", reversed_result)
