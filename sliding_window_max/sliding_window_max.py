from collections import deque
from itertools import islice
'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    '''
    # FIRST PASS SOLUTION
    # window_max = []
    # for i in range(len(nums)-k+1):
    #     window_max.append(max(nums[i:i+k]))
    #     k += 1
    # return window_max
    return [max(nums[i:i+k]) for i in range(len(nums)-k+1)]
    '''
    # WE NEED A QUEUE
    # SET UP INITIAL QUEUE OF length k
        # DECLARE CURRENT MAX
    # ADD TO QUEUE
        # IF VALUE ADDED IS > CURRENT MAX
            # UPDATE CURRENT MAX
        # ELIF VALUE REMOVED WAS THE MAX (== CURRENT MAX)
            # CALCULATE NEW MAX
        # ELSE
            # CURRENT MAX STAYS THE SAME

    window_max = []
    d = deque(nums[:k-1], maxlen=k)
    for i in nums[k-1:]:
        d.append(i)
        window_max.append(max(d))
    return window_max
    '''
    it = iter(nums)
    d = deque(islice(it, k-1), k)
    output = []
    for i in it:
        removed = d[0]
        d.append(i)
        output.append(max(d))
    return output
    '''

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 2

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
