#!/usr/bin/python3
def roman_to_int(roman_string):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    i = 0
    while i < len(roman_string):
        if i + 1 < len(roman_string) and values[roman_string[i]] < values[roman_string[i + 1]]:
                sum += values[roman_string[i + 1]] - values[roman_string[i]]
                i += 2
        else:
            sum += values[roman_string[i]]
            i += 1
    return sum
