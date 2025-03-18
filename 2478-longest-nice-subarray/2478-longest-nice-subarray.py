from itertools import combinations

class Solution(object):
    def longestNiceSubarray(self, nums):
        answer = j = mask = 0
        for i, x in enumerate(nums):
            while mask & x:
                mask ^= nums[j]
                j += 1
            answer = max(answer, i - j + 1)
            
            mask |= x
        return answer