newTuple = ('a', 'b', 'c', 'd', 'e')

def searchTuple(p_tuple, element):
    for i in range(len(p_tuple)):
        if p_tuple[i] == element:
            return f"The element {element} is found at index {i}"
    return 'The element is not found'

print(searchTuple(newTuple, 'b'))
