class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_val, t_val = 0, 0

        for c in s:
            s_val += ord(c)

        for c in t:
            t_val += ord(c)

        return s_val == t_val