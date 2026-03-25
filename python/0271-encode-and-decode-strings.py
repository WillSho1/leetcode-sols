class Solution:

    def encode(self, strs: List[str]) -> str:
        # length prefixing
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # find first prefix starting at i
            j = s.find('#', i)
            # number is i:j
            length = int(s[i:j])
            res.append(s[j+1:j+length+1])
            # move i to end of word
            i = j+length+1
        
        return res

# before used solution where joined ord of chars together into string, and added delimiter between words