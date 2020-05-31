"""
You want your island to have an equal distribution of all 
different types of trees, so your plan is to focus on 
planting trees with the smallest population first. Each 
specific type of tree will be given an int ID. For example, 
1→ apples, 2→ pears, 3 → cherries, etc. Given an array of 
ints that represent the type of tree, return the ID of the 
tree with the smallest population. If there is a tie with 
the smallest population, return the smallest ID.
"""


def getSmallestPopulation(trees):
    occurrence = dict()
    tree = trees[0]
    for i in range(len(trees)):
        occurrence[trees[i]] = occurrence.get(trees[i], 0) + 1
    for key in occurrence:
        if occurrence[tree] == occurrence[key]:
            tree = min(tree, key)
        else:
            if occurrence[tree] > occurrence[key]:
                tree = key
    return tree


def main():
    print(getSmallestPopulation([1, 1, 2, 3, 5, 3, 5, 3, 5]))
    print(getSmallestPopulation([5, 7, 8, 6, 6, 5]))
    print(getSmallestPopulation([1, 3, 1]))
    print("The values above should be 2, 7, and 3.")
