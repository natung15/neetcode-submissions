class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums) #values we have gone through
        if len(seen) == 0:
            return 0
        answer = 1 #return value
        for x in seen:# iterate through array
            if x-1 in seen:
                continue
            y = 1 #how long of a chain / longestConsecutive
            while x+y in seen: #if the current value+1 meaning there is a chain increment
                y+=1 #increment y to see the next value
            answer= max(answer,y)
        return answer
