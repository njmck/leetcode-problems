# My solution:

# Official solution:
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2



l1 = [1, 2, 4]
l2 = [1, 3, 4]

hey = Solution.mergeTwoLists(l1, l1, l2)

print(Solution.mergeTwoLists(l1, l2))
# Output: [1,1,2,3,4,4]

l1 = []
l2 = []
# Output: []

l1 = []
l2 = [0]
# Output: [0]
