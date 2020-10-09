'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
from functools import reduce


def single_number(arr):
    # Your code here
    # use list comprehension to filter list to contain the index with the value that appears only once
    # arr = [x for x in arr if arr.count(x) == 1]

    # use a reducer function to compare each number with the other numbers using the EXOR operator
    # the EXOR will return false for any value that is not exclusive, removing it

    res = reduce(lambda x, y: x ^ y, arr)
    return res
    # return the zero index of the array because that will be the only index in the list, and it will be the only number that was not a duplicate from the original array

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")