#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_x = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rom_num = 0

    for i, char in enumerate(roman_string):
        if i > 0 and roman_x[char] > roman_x[roman_string[i - 1]]:
            rom_num += roman_x[char] - 2 * roman_x[roman_string[i - 1]]
        else:
            rom_num += roman_x[char]

    return rom_num
