
# Approach 1
class Solution:
    def firstUniqChar(self, s: str) -> int:
        countDct = {}
        # Get counts of all letters into dictionary
        for ch in s:
            countDct[ch] = countDct.get(ch, 0) + 1
        # Find first letter from string that is in dictionary and count is 1
        for i, ch in enumerate(s):
            if ch in countDct and countDct[ch] == 1:
                return i
        return -1
    