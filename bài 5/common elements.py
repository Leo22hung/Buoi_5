def common_elements(tuple1, tuple2):
    common = tuple(set(tuple1) & set(tuple2))
    return common

# Example usage:
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
result_tuple = common_elements(tuple1, tuple2)
print("Common elements:", result_tuple)
