'''
Input: an integer
Returns: an integer
'''
'''
FIRST PASS
def eating_cookies(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    counter = 0
    for i in {1,2,3}:
        counter += eating_cookies(n-i)
    return counter
    # single line, list comprehension also works
    # return sum([eating_cookies(n-i) for i in {1,2,3}])
'''

def eating_cookies(n, cache=None):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if not cache:
        cache = {}
    if n in cache:
        return cache[n]
    possibilities = {1,2,3}
    '''
    # FOR LOOP SOLUTION
    total = 0
    for i in possibilities:
        total += eating_cookies(n-i, cache)
    cache[n] = total
    '''
    cache[n] = sum([eating_cookies(n-i, cache) for i in possibilities])
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
