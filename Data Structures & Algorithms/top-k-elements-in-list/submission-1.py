class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # even better soln: lets do a bucketsort for O(n) time!
        counts = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            counts[n] += 1
        for n, c in counts.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res