"""
You are entering a tree growing competition and you are going to 
stun the competition with your magical trees! The objective is 
to enter the tallest tree. Unfortunately, these trees grow in a 
weird way and it will be hard to time when your tree is at its 
tallest. After studying these trees for a while, you realize 
the trees grow according to a function:
Each day:
If the height is one, die.
If the height is a multiple of three, divide the height by three 
If the height is even, subtract one
Otherwise, double your height.
Only one rule applies at a time; whichever rule comes first in the 
list above will be applied. You only have n days before the 
competition (the nth day is the day before the competition). 
Decide which day to plant your tree to get the maximum height 
achievable for the competition. Return days + 1 if the height 
of your tree is at its maximum at day 0 (before planting it). 
"""


def getMaximumHeight(days, height):
    heights = [0] * (days + 1)
    heights[0] = height
    for i in range(1, days + 1):
        if heights[i - 1] == 1:
            break
        elif heights[i - 1] % 3 == 0:
            heights[i] = heights[i - 1] // 3
        elif heights[i - 1] % 2 == 0:
            heights[i] = heights[i - 1] - 1
        else:
            heights[i] = heights[i - 1] * 2
    return days - heights.index(max(heights)) + 1


def main():
    print(getMaximumHeight(5, 11))
    print(getMaximumHeight(5, 8))
    print(getMaximumHeight(6, 1))
    print("The values above should be 5, 2, and 6.")
