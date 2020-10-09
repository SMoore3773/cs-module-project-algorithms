'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
from functools import reduce
from collections import deque

def sliding_window_max(nums, k):
    # Your code here
    # section off a section of the array that is k numbers in length
    # add those numbers together, then push that value to separate array
    # move 'window' right, then repeat previous step until end of window is end of array
    # return array of max values

    # maxArr = [max(nums[i:i+k]) for i in range(len(nums)-k+1)]
    
    maxVals = []
    q = deque()

    # remove all elements from a queue
    for i, n in enumerate(nums):
        while len(q) > 0 and n > q[-1]:
            q.pop()
        q.append(n)

        # calculate window range
        winRange = i - k + 1

        # as long as our window range is == k, then we will add elements to the queue
        if winRange >= 0:
            # add the maximum element ( in this case it will be the first in the queue)
            maxVals.append(q[0])

            # check num on the left is needs to be evicted
            # if so take it out of the start of the queue
            if nums[winRange] == q[0]:
                q.popleft()
    return maxVals

    # maxArr = []
    # i = 0
    # maxNum = -9999999999999999
    # while i + k <= len(nums):
    #     win = nums[i:i+k]
    #     maxInWin = max(win)
        
    #     if maxInWin == win[0]:
    #         maxArr.append(maxInWin)
    #         i += 1
    #     if maxInWin == win[1]:
    #         if i + k + 2 > len(nums):
    #             maxArr.append(maxInWin)
    #             i+=1
    #         else: 
    #             maxArr.append(maxInWin)
    #             maxArr.append(maxInWin)
    #             i += 2
    #     if maxInWin == win[2]:
    #         if i + k + 2 > len(nums):
    #             maxArr.append(maxInWin)
    #             i+=1
    #         if i + k + 3 > len(nums):
    #             maxArr.append(maxInWin)

    #             i+=2
    #         else:
    #             maxArr.append(maxInWin)
    #             maxArr.append(maxInWin)
    #             i += 3

    
    # sumMax = 0
    # maxArr = []
    # # print(nums)
    # for i in range(len(nums)-k+1):
    #     window = nums[i:i+k]
    #     maxArr.append(max(window))

    #     winTotal = reduce((lambda x, y: x+y), window)
    #     if sumMax <= winTotal:
    #         maxArr = window
    #         sumMax = winTotal
    #         arrMaxes.append(sumMax)
    # print(arrMaxes)
    return maxArr



    


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
