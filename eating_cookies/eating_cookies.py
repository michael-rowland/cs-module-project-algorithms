'''
Input: an integer
Returns: an integer
'''
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

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
