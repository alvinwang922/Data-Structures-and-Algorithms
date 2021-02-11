"""
Given a list of n integers arr[0..(n-1)], determine the number 
of different pairs of elements within it which sum to k. If an 
integer appears in the list multiple times, each copy is 
considered to be different; that is, two pairs are considered 
different if one pair includes at least one array index which 
the other doesn't, even if they include the same values.
"""


from collections import defaultdict


def numberOfWays(arr, k):
    tracker, ans = defaultdict(int), 0
    for num in arr:
        if num in tracker:
            ans += tracker[num]
        tracker[k - num] += 1
    return ans


print(numberOfWays([1, 2, 3, 4, 3], 6))
print(numberOfWays([1, 5, 3, 3, 3], 6))
print("The values above should be 2 and 4.")
