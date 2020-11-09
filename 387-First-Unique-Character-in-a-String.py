'''
Leetcode Q387- https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
'''
# Approach 1
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         countDct = {}
#         # Get counts of all letters into dictionary
#         for ch in s:
#             countDct[ch] = countDct.get(ch, 0) + 1
#         # Find first letter from string that is in dictionary and count is 1
#         for i, ch in enumerate(s):
#             if ch in countDct and countDct[ch] == 1:
#                 return i
#         return -1

# Approach 2
class Solution:
    def firstUniqChar(self, s: str) -> int:
        seenSet = set()
        
        # Store letter and it's index
        indexDct = {}
        
        for i, ch in enumerate(s):
            # If not seen before, add to dict along with its index
            if ch not in seenSet:
                indexDct[ch] = i
                seenSet.add(ch)
            # If already seen and exists in dict, delete from dict
            elif ch in indexDct:
                del indexDct[ch]
        # Dict now has index of all single letters, take min of values to get first index
        return min(indexDct.values()) if indexDct else -1   

# Time complexity is O(n). Space complexity is O(n).