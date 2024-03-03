def insert_value_at_beginning(original_tuple, value):
    new_tuple = (value,) + original_tuple
    return new_tuple

# Example usage:
original_tuple = (2, 3, 4)
value = 1
result_tuple = insert_value_at_beginning(original_tuple, value)
print("New tuple:", result_tuple)
