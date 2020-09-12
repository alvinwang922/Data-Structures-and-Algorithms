"""
We need you to quickly identify the list of potential attackers based on 
their email addresses. If an email is not in the edu domain or is not in 
the list of given schools, flag them as an attacker!
Input Format
The first line will contain two integers N and M, denoting the number of 
email address and approved schools respectively.
The next M lines will be the names of the approved schools, using 
only lowercase letters.
The next N lines will be the email addresses. You can assume they will 
all follow the format "name@school.domain" and will only contain lowercase 
letters, one @ sign, and one period. Each email address will also be unique.
"""


num = input().split()
num1, num2 = int(num[0]), int(num[1])
schools = set()
emails = []
for i in range(num2):
    schools.add(input())
for i in range(num1):
    emails.append(input())
for email in emails:
    index1 = email.find("@")
    index2 = email.find(".")
    if email[index1 + 1:index2] not in schools or email[index2 + 1:] != "edu":
        print(email)


"""
Sample input:
10 2
uci
ucsd
rrobert@ucsd.edu
hackerman@uci.xyz
ganderson@uci.edu
ucikid@ucsd.edu
wlin@mit.edu
lnguyen@ucsd.edu
jstrokes@uci.edu
rcampbell@ucsd.edu
ckarthik@uci.edu
ppaul@uci.edu

Sample output:
hackerman@uci.xyz
wlin@mit.edu
"""
