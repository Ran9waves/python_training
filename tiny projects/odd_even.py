def isOdd(number):
    #Returns True if a number is odd and False if a number is even.
    #Also returns False with fractional parts i.e. 3.15, 5.6...
    return number % 2 == 1

def isEven(number):
    #Returns True if a number is even and False if a number is odd.
    #Also returns False with fractional parts i.e. 3.15, 5.6...
    #Zero is considered even.
    return number % 2 == 0
    

#Python assert will stio the program if their condition is False.
assert isOdd(42) == False
assert isOdd(9999) == True
assert isOdd(-10) == False
assert isOdd(-11) == True
assert isOdd(3.1415) == False
assert isEven(42) == True
assert isEven(9999) == False
assert isEven(-10) == True
assert isEven(-11) == False
assert isEven(3.1415) == False

def run_both():
    print(isOdd(4))
    print(isEven(3))

run_both()