class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans i = nums i 
        # ans i + n = nums i so bsicaly concat the two arrays

        # n = len(nums)

        # concat = [0] * (2 * n)

        # for i in range(len(nums)):
        #     concat[i] = nums[i]
        #     concat[i + n] = nums[i]

        # return concat

        return nums * 2