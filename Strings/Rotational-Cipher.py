"""
One simple way to encrypt a string is to "rotate" every alphanumeric 
character by a certain amount. Rotating a character means replacing 
it with another character that is a certain number of steps away in 
normal alphabetic or numerical order. For example, if the string 
"Zebra-493?" is rotated 3 places, the resulting string is 
"Cheud-726?". Every alphabetic character is replaced with the 
character 3 letters higher (wrapping around from Z to A), and every 
numeric character replaced with the character 3 digits higher 
(wrapping around from 9 to 0). Note that the non-alphanumeric 
characters remain unchanged. Given a string and a rotation factor, 
return an encrypted string.
"""


def rotationalCipher(input, rotation_factor):
    input = list(input)
    for i in range(len(input)):
        c = input[i]
        if c.isdigit():
            input[i] = str((int(c) + rotation_factor) % 10)
        elif c.isalpha():
            if 65 <= ord(c) <= 90:
                curr = (ord(c) + (rotation_factor % 26)) % 91
                if curr < 26:
                    curr += 65
                input[i] = chr(curr)
            elif 97 <= ord(c) <= 122:
                curr = (ord(c) + (rotation_factor % 26)) % 123
                if curr < 26:
                    curr += 97
                input[i] = chr(curr)
    return "".join(input)


print(rotationalCipher("Zebra-493?", 3))
print(rotationalCipher("abcdefghijklmNOPQRSTUVWXYZ0123456789", 39))
print(rotationalCipher("abcdZXYzxy-999.@", 200))
print("The strings above should be \"Cheud-726?\", \
    \"nopqrstuvwxyzABCDEFGHIJKLM9012345678\", and \
    \"nopqrstuvwxyzABCDEFGHIJKLM9012345678\".")
