class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for x in strs:
            sortedWord = "".join(sorted(x))
            if sortedWord not in dict:
                dict[sortedWord] = []
            dict[sortedWord].append(x)
        return list(dict.values())