class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dic, t_dic = {}, {}

        for c in s:
            s_dic[c] = s_dic.get(c, 0) + 1
        for c in t:
            t_dic[c] = t_dic.get(c, 0) + 1

        return s_dic == t_dic