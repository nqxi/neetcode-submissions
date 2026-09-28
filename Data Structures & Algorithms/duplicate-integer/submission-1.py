class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # hash if a bucket has more than one of them
        s = set()

        for n in nums:
            if n in s:
                return False
            s.add(n)




        return True
