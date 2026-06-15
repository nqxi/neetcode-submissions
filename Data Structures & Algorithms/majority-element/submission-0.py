class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Hash map soln (unoptimal space wise)
        counts = {}

        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        for key, value in counts.items():
            if value > len(nums) / 2:
                return key
        