class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        answer = 0

        for x in seen:
            if x-1 in seen:
                continue
            y = 1

            while x+y in seen:
                y+=1
            answer= max(answer,y)
        return answer