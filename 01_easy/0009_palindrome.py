# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is palindrome while 123 is not.

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false

x = 121

def isPalindrome(x):
    if str(x)[::-1] != str(x):
        return False
    else:
        return True

print(isPalindrome(x))

# Highest voted solution:

x = 121

def isPalindrome(x):
    # A negative number can never be a palindrome because of '-'.
    if x < 0:
        return False

    # while 121 / 10 (12.1) > 10
    # 1 *= 10
    ranger = 1
    while (x / ranger) >= 10:
        ranger *= 10

    while x:
        left = x / ranger
        right = x % 10
        if left != right:
            return False

        x = (x % ranger) / 10
        ranger /= 100

    return True

print(isPalindrome(x))
