class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        answer = 0
        for x in s:
            if x in seen:
                seen = seen[seen.index(x) + 1:]
            seen.append(x)
            answer = max(answer,len(seen))
        return answer