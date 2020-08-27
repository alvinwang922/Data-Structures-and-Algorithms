"""
We have a collection of stones, each stone has a positive integer weight.
Each turn, we choose the two heaviest stones and smash them together.  
Suppose the stones have weights x and y with x <= y.  
The result of this smash is:
If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, 
and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  
Return the weight of this stone (or 0 if there are no stones left.)
"""


class Solution:
    def lastStoneWeight(self, stones: List[int]):
        for i in range(len(stones) - 1):
            stones.sort()
            stones.append(stones.pop() - stones.pop())
        return stones[0]


print(lastStoneWeight([2, 7, 4, 1, 8, 1]))
print(lastStoneWeight([2, 7, 4, 1]))
print(lastStoneWeight([1, 2, 7, 8, 9, 5, 1]))
print("The values above should be 1, 0, and 1.")
