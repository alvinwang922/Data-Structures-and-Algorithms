"""
You are given an array arr of N integers. For each index i, 
you are required to determine the number of contiguous 
subarrays that fulfills the following conditions: The value 
at index i must be the maximum element in the contiguous 
subarrays, and these contiguous subarrays must either start 
from or end on index i.
"""


def count_subarrays(arr):
    l = len(arr)
    ans = [1] * l
    stack = [-1]
    for i in range(l):
        while len(stack) > 1 and arr[stack[-1]] < arr[i]:
            stack.pop()
        ans[i] += i - stack[-1] - 1
        stack.append(i)
    stack = [l]
    for i in range(l - 1, -1, -1):
        while len(stack) > 1 and arr[stack[-1]] < arr[i]:
            stack.pop()
        ans[i] += stack[-1] - i - 1
        stack.append(i)
    return ans


print(count_subarrays([3, 4, 1, 6, 2]))
print(count_subarrays([2, 4, 7, 1, 5, 3]))
print("The arrays above should be [1, 3, 1, 5, 1] and \
    [1, 2, 6, 1, 3, 1].")
