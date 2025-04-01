class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = []
        for i, x in enumerate(nums):
            l.append((i, x))

        for i in combinations(l, 2):
            if i[0][1] + i[1][1] == target:
                return [i[0][0], i[1][0]] 