"""
Numeros the Artist had two lists that were permutations of one another. He was very proud. 
Unfortunately, while transporting them from one exhibition to another, some numbers were 
lost out of the first list. Can you find the missing numbers?
Notes:
If a number occurs multiple times in the lists, you must ensure that the frequency of that 
number in both lists is the same. If that is not the case, then it is also a missing number.
You have to print all the missing numbers in ascending order.
Print each missing number once, even if it is missing multiple times.
The difference between maximum and minimum number in the second list is less than or equal to 100.
"""


import collections

# Complete the missingNumbers function below.


def missingNumbers(arr, brr):
    ans = []
    if len(arr) > len(brr):
        arr, brr = collections.Counter(arr), collections.Counter(brr)
    else:
        brr, arr = collections.Counter(arr), collections.Counter(brr)
    for num in sorted(arr.keys()):
        if arr[num] != brr[num]:
            ans.append(num)
    return ans


print(missingNumbers([11, 4, 11, 7, 13, 4, 12, 11, 10, 14],
                     [11, 4, 11, 7, 3, 7, 10, 13, 4, 8, 12, 11, 10, 14, 12]))
print(missingNumbers([203, 204, 205, 206, 207, 208, 203, 204, 205, 206],
                     [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]))
print("The lists above should be [3, 7, 8, 10, 12] and [204, 205, 206].")
