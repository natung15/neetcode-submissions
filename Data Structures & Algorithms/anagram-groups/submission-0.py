class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}
        for x in strs:
            key = "".join(sorted(x))
            if key not in answer:
                answer[key] = []
            answer[key].append(x)
        return list(answer.values())