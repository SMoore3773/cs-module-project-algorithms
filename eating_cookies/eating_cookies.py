'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    #base case of no cookies
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    # #eats 1 cookie
    # eating_cookies(n-1)

    # #eats 2 cookies
    # eating_cookies(n-2)

    # #eats 3 cookies
    # eating_cookies(n-3)
    # recursive case where there are still cookies available
    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 4

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
