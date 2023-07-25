#roman_to_integers
# I V  X  L  C  D     M
# 1 5 10 50 100 500 1000
#
class Roman_to_integers:
    def roman_to_int(self, roman_number):
        if not isinstance(roman_number, str):
            raise Exception('variable roman_number must be string')
        numbers = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_number = roman_number.replace('IV', 'IIII')
        roman_number = roman_number.replace('IX', 'VIIII')
        roman_number = roman_number.replace('XL', 'XXXX')
        roman_number = roman_number.replace('XC', 'LXXXX')
        roman_number = roman_number.replace('CD', 'CCCC')
        roman_number = roman_number.replace('CM', 'DCCCC')
        arabic_number =0
        for roman_caracter in roman_number:
            arabic_number += numbers[roman_caracter]
        return arabic_number

numar= Roman_to_integers()

assert numar.roman_to_int('III') ==3,'Expected result shoud be 3'
assert numar.roman_to_int('LVIII') == 58
assert numar.roman_to_int('IV') == 4
assert numar.roman_to_int('IX') == 9
assert numar.roman_to_int('XL') == 40
assert numar.roman_to_int('XC') ==90
assert numar.roman_to_int('CD') == 400
assert numar.roman_to_int('CM')== 900
assert numar.roman_to_int('MCMXCIV') ==1994






