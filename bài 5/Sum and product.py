def sum_and_product(numbers):
    total_sum = sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    return total_sum, product

# Example usage:
my_tuple = (1, 2, 3, 4)
result_sum, result_product = sum_and_product(my_tuple)
print("Sum:", result_sum)
print("Product:", result_product)
