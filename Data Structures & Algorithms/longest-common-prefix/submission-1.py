class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(strs, key=len)
        strs.remove(smallest)

        for s in strs:
            for i in range(len(smallest)):
                if s[i] != smallest[i]:
                    return smallest[:i]
        
        return smallest
