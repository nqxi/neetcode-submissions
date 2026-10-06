class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # no division solution ( saw hints )
        prefs, sufs, res = [], [], []
        # populate prefs
        val = 1
        for n in nums:
            prefs.append(val)
            val = val * n

        val = 1
        for n in reversed(nums):
            sufs.append(val)
            val = val * n
        sufs.reverse()

        for i in range(len(nums)):
            # Multiply prefix and suffix
            res.append(prefs[i] * sufs[i])

        return res
            
