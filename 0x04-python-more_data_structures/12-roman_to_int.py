#!/usr/bin/python3
def roman_to_int(roman_string):
    """This funcion converts roman numerals to integers
     variables:
      Result: stores the outcome of the roman numerals
      Num: A dicionary that uses roman numerals as keys and\
              their corresponding integers as values
    """
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0
    roman_string = roman_string.upper()
    result = 0
    num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(len(roman_string)):
        value = num[roman_string[i]]
        if (i + 1) < len(roman_string) and num[roman_string[i + 1]] > value:
            result -= value
        else:
            result += value
    return result
