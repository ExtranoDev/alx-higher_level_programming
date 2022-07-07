#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        total = 0
        temp = 0
        roman_dict = {
                'M': 1000,
                'D': 500,
                'C': 100,
                'L': 50,
                'X': 10,
                'V': 5,
                'I': 1
                }
        for i in reversed(roman_string):
            temp = roman_dict[i]
            total += temp if total < temp * 5 else -temp
        return total
    return 0
