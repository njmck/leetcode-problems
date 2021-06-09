class Solution:
    def reverse(self, x: int) -> int:

# Input: x = 123
# Output: 321

# Input: x = -123
# Output: -321

# Input: x = 120
# Output: 21

# Input: x = 0
# Output: 0

# Input: 1534236469
# Output: 9646324351

x = 1534236469

def reverse(x):
    input_str = str(x)
    if x >= 0:
        rev = int(input_str[::-1])
    else:
        rev = -1 * int(input_str[::-1][:-1])
    # Return value:
    if -pow(2, 31) <= rev <= pow(2, 31) - 1:
        return rev
    else:
        return 0

print(reverse(x))

# Highest voted solution:

def reverse(x):
    result = 0

    if x < 0:
        symbol = -1 # Add minus symbol
        x = -x
    else:
        symbol = 1

    while x:
        result = result * 10 + x % 10
        x /= 10

    return 0 if result > pow(2, 31) else result * symbol
