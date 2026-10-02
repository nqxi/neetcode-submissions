class Solution:
    #LETS SOLVE TWO SUM :D
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = {}
        for i, n in enumerate(nums):
            # if it is the complement already there
            if n in c:
                return [c[n], i]
            c[target-n] = i