from itertools import combinations
class Solution(object):
    def twoSum(self, nums, target):
        l = []
        for i, x in enumerate(nums):
            l.append((i, x))
        for k in combinations(l, 2):
            if k[0][1] + k[1][1] == target:
                return [k[0][0], k[1][0]]