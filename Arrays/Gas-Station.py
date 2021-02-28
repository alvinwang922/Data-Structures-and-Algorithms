"""
There are N gas stations along a circular route, where 
the amount of gas at station i is gas[i]. You have a 
car with an unlimited gas tank and it costs cost[i] 
of gas to travel from station i to its next station 
(i+1). You begin the journey with an empty tank at 
one of the gas stations. Return the starting gas 
station's index if you can travel around the circuit 
once in the clockwise direction, otherwise return -1.
"""


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) == 0 or len(cost) == 0 or sum(gas) < sum(cost):
            return -1
        else:
            position = 0
            balance = 0
            for i in range(len(gas)):
                balance += gas[i] - cost[i]
                if balance < 0:
                    balance = 0
                    position = i + 1
            return position

    print(canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    print(canCompleteCircuit([2, 3, 4], [3, 4, 3]))
    print(canCompleteCircuit([], [1]))
    print("The values above should be 3, -1, and -1.")
