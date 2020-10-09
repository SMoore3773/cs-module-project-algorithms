'''
Input: a List of integers
Returns: a List of integers
'''
# run backwards 

def moving_zeroes(arr):
    tempzero = []
    tempnum = []
    for i in range(0, len(arr)):
        if arr[i] == 0:
            tempzero.append(arr[i])
        else:
            tempnum.append(arr[i])
    tempnum.extend(tempzero)

    return tempnum


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
