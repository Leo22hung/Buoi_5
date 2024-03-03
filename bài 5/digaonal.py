def diagonal_elements(tuple_of_tuples):
    diagonal = tuple(tuple_of_tuples[i][i] for i in range(min(len(tuple_of_tuples), len(tuple_of_tuples[0]))))
    return diagonal

# Example usage:
tuple_of_tuples = ((1, 2, 3),
                   (4, 5, 6),
                   (7, 8, 9))

result_tuple = diagonal_elements(tuple_of_tuples)
print("Diagonal elements:", result_tuple)
