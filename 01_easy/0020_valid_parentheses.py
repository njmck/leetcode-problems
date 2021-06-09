# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:
# Input: s = "()"
# Output: true
#
# Example 2:
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
# Input: s = "(]"
# Output: false
#
# Example 4:
# Input: s = "([)]"
# Output: false
#
# Example 5:
# Input: s = "{[]}"
# Output: true

# Make the dictionary and appropriate list:
def isValid(s):
    dict = {
        '(': 0,
        ')': 0,
        '{': 0,
        '}': 0,
        '[': 0,
        ']': 0
    }
    key_list = [_ for _ in dict]
    # Do the brackets counting:
    for i_0 in s:
        dict[i_0] += 1
    # Test if the brackets are closed:
    brackets_closed = True
    i_0 = 0
    while i_0 < len(key_list):
        if dict[key_list[i_0]] != dict[key_list[i_0 + 1]]:
            brackets_closed = False
        i_0 += 2
    return brackets_closed

s = "()[]{}"
print(isValid(s))

s = "([)]"
print(isValid(s))
