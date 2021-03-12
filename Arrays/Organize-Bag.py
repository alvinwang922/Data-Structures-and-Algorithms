"""
You want to organize your bag by putting all your prized 
fish and bugs in one section of your bag. Given an array 
representing all the items in your bag, move all your prized 
catches (represented by the number 0) to the right of the 
bag while maintaining the relative order of the other items. 
"""


def organizeBag(bag):
    for i in range(len(bag)):
        if bag[i] == 0:
            for j in range(i, len(bag) - 1):
                bag[j] = bag[j + 1]
            bag[len(bag) - 1] = 0
    return bag

    print(organizeBag([0, 1, 0, 3, 12]))
    print(organizeBag([5, 4, 0]))
    print(organizeBag([0, 1]))
    print("The arrays above should be [1, 3, 12, 0, 0], \
         [5, 4, 0], and [1, 0].")
