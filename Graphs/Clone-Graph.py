# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a val (int) and a list
# (List[Node]) of its neighbors.

import collections

# Definition for a Node.


class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Implemented with BFS
class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return
        copy = {node: Node(node.val)}
        element = collections.deque([node])
        while element:
            for i in range(len(element)):
                currNode = element.popleft()
                for neigh in currNode.neighbors:
                    if neigh not in copy:
                        copy[neigh] = Node(neigh.val)
                        element.append(neigh)
                    copy[currNode].neighbors.append(copy[neigh])
        return copy[node]

    print(cloneGraph([[2, 4], [1, 3], [2, 4], [1, 3]]))
    print(cloneGraph([[]]))
    print(cloneGraph([]))
    print(cloneGraph([[2], [1]]))
    print("The graphs above should be [[2,4],[1,3],[2,4],[1,3]],\
        [[]],[],and [[2],[1]].")
