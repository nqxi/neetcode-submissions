class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        s_frq = {}
        t_frq = {}

        for c in s:
            s_frq[c] = s_frq.get(c, 0) + 1

        for c in t:
            t_frq[c] = t_frq.get(c, 0) + 1


        print(s_frq, t_frq)
        for key in s_frq:
            if s_frq.get(key) != t_frq.get(key):
                return False



        return True
