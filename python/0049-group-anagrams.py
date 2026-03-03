from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # n*mlogm would be sorting all words in list
        ana_dict = dict()
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in ana_dict.keys():
                ana_dict[sorted_word] = [word]
            else:
                ana_dict[sorted_word].append(word)
        return ana_dict.values()