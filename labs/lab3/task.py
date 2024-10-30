def adjacent_elements_product(array):
    max_product = array[0] * array[1]
    for i in range(1, len(array) - 1):
        product = array[i] * array[i + 1]
        if product > max_product:
            max_product = product
    return max_product

print(adjacent_elements_product([1, 2, 3]))
print(adjacent_elements_product([9, 5, 10, 2, 24, -1, -48]))
print(adjacent_elements_product([-23, 4, -5, 99, -27, 329, -2, 7, -921]))  

