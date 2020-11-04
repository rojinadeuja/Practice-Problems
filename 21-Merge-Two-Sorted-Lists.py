'''
Leetcode Q21 -https://leetcode.com/problems/merge-two-sorted-lists/
Merge two sorted linked lists and return it as a new sorted list. 
The new list should be made by splicing together the nodes of the first two lists.
'''

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
        