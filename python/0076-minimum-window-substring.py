class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # get required counts
        countT = {}
        for char in t:
            countT[char] = countT.get(char, 0)+1
        
        # dict for freq of window
        window = {}
        left = 0

        # keep track of have/need counts
        have = 0
        need = len(countT)
        minWindow = None
        for right in range(len(s)):
            # update the window
            window[s[right]] = window.get(s[right], 0)+1

            # update have
            if s[right] in countT and countT[s[right]] == window[s[right]]:
                have += 1
            
            print(f"current char: {s[right]}, HAVE: {have}")
            # while substring contains letters
            while have == need:
                if minWindow == None or right+1-left < minWindow[1]+1-minWindow[0]:
                    minWindow = [left, right]

                window[s[left]] -= 1
                if s[left] in countT and countT[s[left]] > window[s[left]]:
                    have -= 1
                left += 1
        return s[minWindow[0]:minWindow[1]+1] if minWindow!=None else ""
                

"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        for char in t:
            countT[char] = countT.get(char, 0)+1
        
        window = {}
        left = 0
        # track amount of matches necessary
        need = len(countT)
        # track amount you have
        have = 0
        res = [-1, -1]
        for right in range(len(s)):
            # update the window

            # check if you have what you need

            # while you have what you need
                # update res if shorter

                # shrink window
                # update have
        
        # return
        """