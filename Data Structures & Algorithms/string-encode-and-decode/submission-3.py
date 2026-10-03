class Solution:
    # Lowkey idk what this expects. reading hint 3 made it make sense (just put a payload at the front rather than delimiting)
    def encode(self, strs: List[str]) -> str:
        lengths = []
        for s in strs:
            lengths.append(str(len(s)))
            lengths.append(';')
        if len(lengths) > 0:
            lengths.pop()
        lengths.append('#')

        header = ''.join(lengths)
        body = ''.join(strs)
        return header + body

        
    def decode(self, s: str) -> List[str]:
        s = s.split('#', 1) 
        header = [x for x in s[0] if x != '']
        lengths = [int(n) for n in header.split(';')]
        body = s[1]

        res = []
        i = 0
        for l in lengths:
            res.append(body[i:i+l])
            i += l

        return res


