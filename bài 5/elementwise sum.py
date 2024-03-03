def tuple_elementwise_sum(tuple1, tuple2):
    result = tuple(x + y for x, y in zip(tuple1, tuple2))
    return result

# Example usage:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result_tuple = tuple_elementwise_sum(tuple1, tuple2)
print("Element-wise sum tuple:", result_tuple)
