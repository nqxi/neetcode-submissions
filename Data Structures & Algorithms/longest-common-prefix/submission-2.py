class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(strs, key=len)
        strs.remove(smallest)

        for i in range(len(smallest)):
            ok = True
            for s in strs:
                if s[i] != smallest[i]:
                    ok = False
            if not ok:
                return smallest[:i]
                
        return smallest
