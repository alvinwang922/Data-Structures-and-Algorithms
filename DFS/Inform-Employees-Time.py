"""
A company has n employees with a unique ID for each employee from 0 to n - 1. The head of 
the company has is the one with headID. Each employee has one direct manager given in the 
manager array where manager[i] is the direct manager of the i-th employee, 
manager[headID] = -1. Also it's guaranteed that the subordination relationships have a 
tree structure. The head of the company wants to inform all the employees of the company 
of an urgent piece of news. He will inform his direct subordinates and they will inform 
their subordinates and so on until all employees know about the urgent news. The i-th 
employee needs informTime[i] minutes to inform all of his direct subordinates (i.e 
After informTime[i] minutes, all his direct subordinates can start spreading the news). 
Return the number of minutes needed to inform all the employees about the urgent news.
"""


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]):
        children = defaultdict(list)
        for i in range(len(manager)):
            if manager[i] >= 0:
                children[manager[i]].append(i)

        def dfs(node):
            return max([dfs(child) for child in children[node]] or [0]) + informTime[node]
        return dfs(headID)


print(numOfMinutes(6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]))
print(numOfMinutes(7, 6, [1, 2, 3, 4, 5, 6, -1], [0, 6, 5, 4, 3, 2, 1]))
print(numOfMinutes(15, 0, [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4,
                           5, 5, 6, 6], [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]))
print("The values above should be 1, 21, and 3.")
