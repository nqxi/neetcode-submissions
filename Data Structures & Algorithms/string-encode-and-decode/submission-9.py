class Solution:
    # post-editorial soln
    def encode(self, strs: List[str]) -> str:
        new = []
        for s in strs:
            new.append(str(len(s)) + '#')
            new.append(s)

        return ''.join(new)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            l = int(s[i:j])
            res.append(s[j+1:j+1+l])
            i = j+1+l
        return res