"""
Equations are given in the format A / B = k, where A and B are variables 
represented as strings, and k is a real number (floating point number). Given 
some queries, return the answers. If the answer does not exist, return -1.0.
"""


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float],
                     queries: List[List[str]]):
        self.relation = collections.defaultdict(dict)
        for [i, j], value in zip(equations, values):
            self.relation[i][j] = value
            self.relation[j][i] = 1 / value
        output = []
        for i, j in queries:
            if {i, j}.issubset(self.relation):
                output.append(self.dfs(i, j, 1, set()))
            else:
                output.append(-1)
        return output

    def dfs(self, first, second, temp, visited):
        if first == second:
            return temp
        visited.add(first)
        for next, value in self.relation[first].items():
            if next not in visited:
                ans = self.dfs(next, second, temp * value, visited)
                if ans != -1:
                    return ans
        return -1


print(calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0],
                   [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
print("The array above should be [6.00000, 0.50000, -1.00000, 1.00000, -1.00000].")
