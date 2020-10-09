'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, memo):
    # Your code here
    # base case of no cookies
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in memo:
        return memo[n]
    # #eats 1 cookie
    # eating_cookies(n-1)

    # #eats 2 cookies
    # eating_cookies(n-2)

    # #eats 3 cookies
    # eating_cookies(n-3)
    # recursive case where there are still cookies available
    memo[n] = eating_cookies(n-1, memo) + eating_cookies(n-2, memo) + eating_cookies(n-3, memo)

    return memo[n]

    # building a solution table for the cookie problem

    # sol_table = [0 for _ in range(0, n+3)]
    # sol_table[0] = 1
    # sol_table[1] = 1
    # sol_table[2] = 2

    # for i in range(3, n+2):
    #     sol_table[i] = sol_table[i-1] + sol_table[i-2] + sol_table[i-3]
    # return sol_table[n]





if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 40

    print(f"There are {eating_cookies(num_cookies, {})} ways for Cookie Monster to each {num_cookies} cookies")
