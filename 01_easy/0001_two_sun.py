# Input:

# Input:
# nums = [2,7,11,15]
# target = 9

# Output:
# [0,1]
# Because nums[0] + nums[1] == 9, we return [0, 1].

# In O(n) time:

nums = [2, 7, 11, 15]
target = 9

def twoSum(nums, target):
    d = {}
    for i, n in enumerate(nums):
        m = target - n
        if m in d:
            return [d[m], i]
        else:
            d[n] = i



# My solution:

nums = [2, 7, 11, 15]
target = 9


def twoSum(nums, target)
    for num_0, i_0 in enumerate(nums):
        for num_1, i_1 in enumerate(nums):
            if (num_0 != num_1) and (i_0 + i_1 == target):
                target_ints = [num_0, num_1]
                target_ints.sort()
                return target_ints

x = Solution()

