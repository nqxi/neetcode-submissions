class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord('a')] += 1
            
            chars = tuple(chars)
            if chars not in anagrams:
                anagrams[chars] = []
            anagrams[chars].append(s)
        
        output = []
        for v in anagrams.values():
            output.append(v)

        return output
