class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # this pattern was hard even with careful reading of this shit writing i am a hintslop loser chud
        k = 0
        for n in nums:
            if n != val:
                nums[k]=n
                k += 1

        return k