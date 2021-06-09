# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower", "flow", "flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog", "racecar", "car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longestCommonPrefix(strs):
    common = True
    build_list = []
    num = 0
    shortest = len(min(strs))
    while common == True and num < shortest:
        char = [i_0[num] for i_0 in strs]
        if char.count(char[0]) == len(char):
            build_list.append(char[0])
            num += 1
        else:
            common = False
    # Return the joined list:
    if build_list != []:
        return ''.join(build_list)
    else:
        return ''

strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))

strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))

strs = ['dog', 'doggone', 'doggo']
print(longestCommonPrefix(strs))

# Highest-rated answer:
def longestCommonPrefix(S):
    if not S:
        return ''
    m, M, i = min(S), max(S), 0
    for i in range(min(len(m),len(M))):
        if m[i] != M[i]: break
    else: i += 1
    return m[:i]