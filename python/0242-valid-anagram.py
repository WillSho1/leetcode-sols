class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # base
        if len(s) != len(t):
            return False
        
        count_list = [0] * 26
        for i in range(len(s)):
            count_list[ord(s[i]) - ord("a")] += 1
            count_list[ord(t[i]) - ord("a")] -= 1

        # check
        for count in count_list:
            if count != 0:
                return False

        return True
