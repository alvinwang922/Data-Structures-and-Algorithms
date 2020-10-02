"""
The chess knight has a unique movement, it may move two squares vertically 
and one square horizontally, or two squares horizontally and one square 
vertically (with both forming the shape of an L). We have a chess knight 
and a phone pad as shown below, the knight can only stand on a numeric cell.
Given an integer n, return how many distinct phone numbers of length n we 
can dial. You are allowed to place the knight on any numeric cell initially 
and then you should perform n - 1 jumps to dial a number of length n. All 
jumps should be valid knight jumps. As the answer may be very large, return 
the answer modulo 10^9 + 7.
"""


class Solution:
    def knightDialer(self, n: int):
        movements = {
            0: (4, 6),
            1: (6, 8),
            2: (7, 9),
            3: (4, 8),
            4: (0, 3, 9),
            5: (),
            6: (0, 1, 7),
            7: (2, 6),
            8: (1, 3),
            9: (2, 4)
        }
        total = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        for _ in range(n - 1):
            curr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for num in range(10):
                for move in movements[num]:
                    curr[move] = (curr[move] + total[num]) % (10 ** 9 + 7)
            total = curr
        return sum(total) % (10 ** 9 + 7)


print(knightDialer(3))
print(knightDialer(4))
print(knightDialer(5))
print("The values above should be 46, 104, and 136006598.")
