def same_frequency(list1, list2):
    frequency1 = {}
    for item in list1:
        frequency1[item] = frequency1.get(item, 0) + 1

    frequency2 = {}
    for item in list2:
        frequency2[item] = frequency2.get(item, 0) + 1

    return frequency1 == frequency2

# Example usage:
list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(same_frequency(list1, list2))  