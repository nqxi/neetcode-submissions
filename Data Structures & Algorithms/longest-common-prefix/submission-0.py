class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        w = strs[0]
        for s in strs:
            if len(s) < len(w):
                w = s
                
        shared = len(w)

        for i in range(1, len(strs)):
            for j in range(len(w)):
                if strs[i][j] != w[j]:
                    shared = j
        

        return w[:shared]