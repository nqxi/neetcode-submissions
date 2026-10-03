class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1
        t = sorted(tuple(counts.items()), key = lambda x:x[1], reverse=True)
        
        res = []
        for i in range(k):
            res.append(t[i][0])
        return res