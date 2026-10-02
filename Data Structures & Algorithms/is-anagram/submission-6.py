class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_s, dict_t = defaultdict(int), defaultdict(int)
        for cs, ct in zip(s, t):
            dict_s[cs] += 1
            dict_t[ct] += 1

        return dict_s == dict_t
