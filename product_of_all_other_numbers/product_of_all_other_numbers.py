'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    '''
    # FIRST PASS
    products = []
    for i in arr:
        result = 1
        for j in arr:
            if j == i:
                continue
            result = result * j
        products.append(result)
    return products

    # SECOND PASS
    product = 1
    for i in arr:
        product *= i
    return [int(product/i) for i in arr]
    '''

    products = [0] * len(arr)
    prod = 1
    # loop through all values of array
    for i in range(len(arr)):
        # product of all items before
        products[i] = prod
        prod *= arr[i]

    prod = 1
    for i in range(len(arr)-1, -1, -1):
        products[i] *= prod
        prod *= arr[i]
    
    return products


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
