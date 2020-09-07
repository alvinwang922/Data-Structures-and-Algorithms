"""
Design and implement a data structure for Least Frequently Used 
(LFU) cache. It should support the following operations: get and put.
get(key) - Get the value (will always be positive) of the key if 
the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already 
present. When the cache reaches its capacity, it should invalidate 
the least frequently used item before inserting a new item. For the 
purpose of this problem, when there is a tie (i.e., two or more keys 
that have the same frequency), the least recently used key would be evicted.
Note that the number of times an item is used is the number of calls to the 
get and put functions for that item since it was inserted. This number is 
set to zero when the item is removed.
Follow up: Could you do both operations in O(1) time complexity?
"""


class Node:
    def __init__(self, key=None, val=None, freq=1):
        self.key = key
        self.val = val
        self.f = freq
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.sent = Node()
        self.sent.next = self.sent.prev = self.sent
        self.size = 0

    # number of nodes in the linked list
    def len(self):
        return self.size

    # append a node to the end of the linked list
    def append(self, n: Node):
        (last := self.sent.prev).next = n
        n.prev = last
        n.next = self.sent
        self.sent.prev = n
        self.size += 1

    # removes a node, or the front of the linked list if no node provided
    def remove(self, n: Node = None):
        if self.size == 0:
            return None
        if not n:
            n = self.sent.next
        (left := n.prev).next = (right := n.next)
        right.prev = left
        self.size -= 1
        return n


class LFUCache:
    def __init__(self, capacity: int):
        self.cap = max(0, capacity)
        self.nodes = {}
        self.freqs = defaultdict(LinkedList)
        self.min_freq = 0

    # updates a node's frequency, and updates the min frequency if necessary
    def _update(self, n: Node):
        self.freqs[n.f].remove(n)
        if self.min_freq == n.f and self.freqs[n.f].len() == 0:
            self.min_freq += 1
        n.f += 1
        self.freqs[n.f].append(n)

    def get(self, key: int):
        if key not in self.nodes:
            return -1
        self._update(n := self.nodes[key])
        return n.val

    def put(self, key: int, value: int):
        if self.cap == 0:
            return None
        if key in self.nodes:
            (n := self.nodes[key]).val = value
            self._update(n)
            return
        if len(self.nodes) >= self.cap:
            del self.nodes[self.freqs[self.min_freq].remove().key]
        self.nodes[key] = (n := Node(key, value))
        self.freqs[1].append(n)
        self.min_freq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)       # returns 1
cache.put(3, 3)    # evicts key 2
cache.get(2)       # returns -1 (not found)
cache.get(3)       # returns 3.
cache.put(4, 4)    # evicts key 1.
cache.get(1)       # returns -1 (not found)
cache.get(3)       # returns 3
cache.get(4)       # returns 4
