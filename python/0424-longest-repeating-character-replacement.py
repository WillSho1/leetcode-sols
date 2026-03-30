class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqDict = {}
        maxLength = 0
        left = 0
        maxFreq = 0

        for right in range(len(s)):
            # update the freqDict
            freqDict[s[right]] = freqDict.get(s[right], 0)+1
            # update maxFreq for this window
            maxFreq = max(maxFreq, freqDict[s[right]])
            # the maxFreq is a pseudo solution, does not need to decrease
                # do not need to check every solution
                # keeps window as wide as current solution
                # moves left once on invalid window (no increase to maxF)
                # moves right once in valid window(increase to maxF)

            # check validity of window
            if right+1-left-maxFreq > k:
                # if not valid, move left
                freqDict[s[left]] -= 1
                left += 1
            # if valid, update the maxLength
            else:
                maxLength = max(maxLength, right+1-left)

        return maxLength