'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
from functools import reduce


def sliding_window_max(nums, k):
    # Your code here
    # section off a section of the array that is k numbers in length
    # add those numbers together, then push that value to separate array
    # move 'window' right, then repeat previous step until end of window is end of array
    # return array of max values
    
    maxArr = [max(nums[i:i+k]) for i in range(len(nums)-k+1)]

    maxArr = []
    i = 0
    maxNum = -9999999999999999
    while i + k <= len(nums):
        win = nums[i:i+k]
        maxInWin = max(win)
        
        if maxInWin == win[0]:
            maxArr.append(maxInWin)
            i += 1
        if maxInWin == win[1]:
            if i + k + 2 > len(nums):
                maxArr.append(maxInWin)
                i+=1
            else: 
                maxArr.append(maxInWin)
                maxArr.append(maxInWin)
                i += 2
        if maxInWin == win[2]:
            if i + k + 2 > len(nums):
                maxArr.append(maxInWin)
                i+=1
            if i + k + 3 > len(nums):
                maxArr.append(maxInWin)

                i+=2
            else:
                maxArr.append(maxInWin)
                maxArr.append(maxInWin)
                i += 3

    
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
