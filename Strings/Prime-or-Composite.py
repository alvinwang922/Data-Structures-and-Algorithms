"""
Given a string of numbers separated by spaces, return a string composed 
of the words "Prime" and "Composite" separated by spaces representing 
whether the numbers are prime or composite.
"""


def primeOrComposite(numbers):
    numbers = numbers.split()
    result = ""
    for number in numbers:
        number = int(number)
        if number <= 1:
            result += "Composite "
        elif number <= 3:
            result += "Prime "
        else:
            isPrime = True
            i = 2
            while((i * i) <= number):
                if number % i == 0:
                    isPrime = False
                i += 1
            if isPrime:
                result += "Prime "
            else:
                result += "Composite "
    return result


print(primeOrComposite("2 3 4 5"))
print(primeOrComposite("8 10"))
print(primeOrComposite("49 47 41"))
print("The strings above should be \"Prime Prime Composite Prime\", \
    \"Composite Composite\", and \"Composite Prime Prime\"")
