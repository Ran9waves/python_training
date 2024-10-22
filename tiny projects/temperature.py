#Converting between Celsius and Farenheit

def convertToFarenheit(degreeCelsius):
    #Calculate and return the degrees Farenheit:
    return degreeCelsius * (9 / 5 ) + 32

def convertToCelsius(degreeFarenheit):
    #Calculate and return the degrees Celsius:
    return (degreeFarenheit - 32) * (5 / 9)

#Assert statements stop the program if their condition is False. The solution is correct if the following assert statements' conditions are True

assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFarenheit(0) == 32
assert convertToFarenheit(100) == 212
assert convertToCelsius(convertToFarenheit(15)) == 15

#Rounding errors case a slight discrepancy:
assert convertToCelsius(convertToFarenheit(42)) == 42.00000000000001

print(convertToFarenheit(0))
print(convertToCelsius(0))