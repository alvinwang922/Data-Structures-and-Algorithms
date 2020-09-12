"""
Spending summer cooped up in your house has become quite stifiling. 
You desire anything to get away from those boomers and zoomers 
constantly trying to pry you away from your Minecraft survival 
world. That is why you have decided to book a flight to Earth's 
orbit - a place surely free of Covid-19 - aboard Elon Musk's 
Falcon20. Of course, Mr. Musk, being the very responsible man he 
is, has made sure to adhere to social distancing guidelines. Hence, 
he has prevented the booking of any seats adjacent to one another. 
This means, for this particular spacecraft with six seats per row 
separated in the middle by an aisle, that if a seat is taken, the 
seats directly in front, behind, to the left, or to the right cannot 
be occupied by another passenger. It is, however, acceptable to seat 
passengers directly across the aisle from one another [reference diagram 
for clarity]. This leads you to wonder what the maximum capacity of the 
spacecraft is with these constrictions.
"""


num = int(input())
for i in range(num):
    x = int(input())
    y = x
    x //= 2
    x *= 6
    if y % 2 == 1:
        x += 4
    print(x)

"""
Sample Input 0:
1
2
Sample Output 0:
6
Sample Input 1:
2
10
4
Sample Output 1:
30
12
"""
