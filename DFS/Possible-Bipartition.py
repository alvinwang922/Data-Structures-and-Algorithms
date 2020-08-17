"""
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone 
into two groups of any size. Each person may dislike some other people, and they 
should not go into the same group. Formally, if dislikes[i] = [a, b], it means 
it is not allowed to put the people numbered a and b into the same group. Return 
true if and only if it is possible to split everyone into two groups in this way.
"""


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]):
        graph = defaultdict(list)
        for i, j in dislikes:
            graph[i].append(j)
            graph[j].append(i)

        def dfs(graph, color, node, col):
            color[node] = col
            for neighbor in graph[node]:
                if color[neighbor] == col:
                    return False
                if color[neighbor] == 0 and not dfs(graph, color, neighbor, -col):
                    return False
            return True


print(possibleBipartition(4, [[1, 2], [1, 3], [2, 4]]))
print(possibleBipartition(3, [[1, 2], [1, 3], [2, 3]]))
print(possibleBipartition(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]))
print("The booleans above should be True, False, and False.")
