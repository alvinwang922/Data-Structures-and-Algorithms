"""
Design a data structure that supports all following operations in average O(1) time.
insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements (it's guaranteed that 
at least one element exists when this method is called). Each element must have the 
same probability of being returned.
"""


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.indices = dict()
        self.nums = []

    def insert(self, val: int):
        """
        Inserts a value to the set. Returns true if the set did not already 
        contain the specified element.
        """
        if val not in self.indices:
            self.nums.append(val)
            self.indices[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val: int):
        """
        Removes a value from the set. Returns true if the set contained 
        the specified element.
        """
        if val in self.indices:
            tempLast = self.nums[-1]
            tempRemove = self.indices[val]
            self.nums[tempRemove], self.indices[tempLast] = tempLast, tempRemove
            del self.indices[val]
            del self.nums[-1]
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        """
        return self.nums[randrange(len(self.nums))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


"""
// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
"""
