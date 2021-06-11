# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Example 1:
# Input: s = "III"
# Output: 3
#
# Example 2:
# Input: s = "IV"
# Output: 4
#
# Example 3:
# Input: s = "IX"
# Output: 9
#
# Example 4:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
#
# Example 5:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

s = 'III'
rom_num = "CMXCIV"

# My solution:
values = {"I": 1,
          "V": 5,
          "X": 10,
          "L": 50,
          "C": 100,
          "D": 500,
          "M": 1000,
          }

def romanToInt(s):
    total = 0
    i_0 = 0
    while i_0 < len(s):
        if (i_0 + 1) < len(s) and \
                values[s[i_0 + 1]] > values[s[i_0]]:
            total += values[s[i_0 + 1]] - values[s[i_0]]
            i_0 += 2
        else:
            total += values[s[i_0]]
            i_0 += 1
    return total

print(romanToInt(s))
print(romanToInt(rom_num))

# LeetCode solution:
values = {"I": 1,
          "V": 5,
          "X": 10,
          "L": 50,
          "C": 100,
          "D": 500,
          "M": 1000,
          }

def romanToInt(s):
    total = 0
    i_0 = 0 # i_0 functions simply as a counter for iteration.
    while i_0 < len(s): # While the length of the roman numeral is not reached:
        # If i_0 is less than the length of roman numeral
        # AND
        if ((i_0 + 1) < len(s)) and (values[s[i_0]] < values[s[i_0 + 1]]):
            # Add to total
            total += values[s[i_0 + 1]] - values[s[i_0]]
            i_0 += 2
        # Else this is NOT the subtractive case.
        else:
            total += values[s[i_0]]
            i_0 += 1
    return total

print(romanToInt(s))
print(romanToInt(rom_num))

# Highest-voted answer:
def romanToInt(s):
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0
    # Just replace complex numerals with less complex numerals:
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    # Then just loop through each individual letter and add them up using the dict:
    for char in s:
        number += translations[char]
    # Return final number:
    return number

print(romanToInt(s))
print(romanToInt(rom_num))
