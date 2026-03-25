class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupDict = {}

        for word in strs:
            # compute char frequencies
            count = [0]*26

            for char in word:
                count[ord(char)-ord('a')] += 1

            key = tuple(count)
            if key not in groupDict:
                groupDict[key] = []
            groupDict[key].append(word)

        return [wordList for wordList in groupDict.values()]