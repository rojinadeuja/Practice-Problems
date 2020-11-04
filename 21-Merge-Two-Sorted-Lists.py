# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Combine lists into a sorted list
        comb = []
        while(l1):
            comb.append(l1.val)
            l1=l1.next
        while(l2):
            comb.append(l2.val)
            l2=l2.next
        comb.sort()
        # Convert list to linked list
        res = dummy = ListNode()
        for num in comb:
            res.next = ListNode(num)
            res = res.next
        return (dummy.next)

# Time complexity is O(n). Space complexity is O(n).
        