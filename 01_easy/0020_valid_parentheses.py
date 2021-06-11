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

# Bracket must open and close before another closed bracket:

# Official solution:
def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """

    # The stack to keep track of opening brackets.
    stack = []

    # Hash map for keeping track of mappings. This keeps the code very clean.
    # Also makes adding more types of parenthesis easier
    mapping = {")": "(", "}": "{", "]": "["}

    # For every bracket in the expression.
    for char in s:

        # If the character is an closing bracket
        if char in mapping:

            # Pop the topmost element from the stack, if it is non empty
            # Otherwise assign a dummy value of '#' to the top_element variable
            top_element = stack.pop() if stack else '#'

            # The mapping for the opening bracket in our hash and the top
            # element of the stack don't match, return False
            if mapping[char] != top_element:
                return False
        else:
            # We have an opening bracket, simply push it onto the stack.
            stack.append(char)

    # In the end, if the stack is empty, then we have a valid expression.
    # The stack won't be empty for cases like ((()
    return not stack


s = "()[]{}"
print(isValid(s))

s = "([)]"
print(isValid(s))
