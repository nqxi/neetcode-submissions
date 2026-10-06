class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        counts = defaultdict(list)
        res = [0] * len(nums)

        # handle zero cases
        nz = len([x for x in nums if x == 0])
        nzp = math.prod([x for x in nums if x != 0])
        # first case one zero
        if nz == 1:
            return [nzp if n==0 else 0 for n in nums]
        # any more and its all zeroes
        if nz >= 2:
            return res

        p = math.prod(nums)

        for idx, n in enumerate(nums):
            counts[n].append(idx)
        # {n = [i1, i2 ... ik]}

        for n, v in counts.items():
            for k in v:
                res[k] = int(p / n) # easy soln (using division - next part is to not use it)


        return res
        

