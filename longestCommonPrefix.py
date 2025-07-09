from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        p_len = len(prefix)

        for i in range(1, len(strs)):
            while prefix != strs[i][:p_len]:
                p_len -= 1
                if p_len == 0:
                    return ""
                prefix = prefix[0:p_len]
        
        return prefix