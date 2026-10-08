class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedList = {}

        for x in strs:
            sortedWord = "".join(sorted(x))
            if sortedWord not in sortedList:
                sortedList[sortedWord] = []
            sortedList[sortedWord].append(x)
        return list(sortedList.values())
