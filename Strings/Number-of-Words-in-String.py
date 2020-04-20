# Given a string, "Hello this is a string" write me a method to return the count of words in that string
# Input: "Hello this is a string" -->  5
# Caviotte, you cannot use any bulit methods such as split, and no built in functions


def numberOfWords(words):
    isSpace = True
    counter = 0
    for i in range(len(words)):
        if words[i] != " " and isSpace == True:
            counter += 1
            isSpace = False
        else:
            isSpace = True
    return counter


print(numOfWords("This has  random   spaces"))
print(numOfWords("  Spaces at front and end   "))
print(numOfWords("        "))
print("The values above should be 4, 5, and 0.")
