'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    """ FIRST PASS
    # zeroes = [i for i in arr if i == 0]
    # nonzeroes = [i for i in arr if i != 0]
    # return nonzeroes + zeroes
    return [i for i in arr if i != 0] + [i for i in arr if i == 0]
    """
    left, right = 0, len(arr)-1
    while left < right:
        if arr[left] == 0 and arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        else:
            if arr[left] != 0:
                left += 1 
            if arr[right] == 0:
                right -= 1
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")