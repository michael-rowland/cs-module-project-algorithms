'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    zeroes = [i for i in arr if i == 0]
    nonzeroes = [i for i in arr if i != 0]
    # return nonzeroes + zeroes
    return [i for i in arr if i != 0] + [i for i in arr if i == 0]

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")