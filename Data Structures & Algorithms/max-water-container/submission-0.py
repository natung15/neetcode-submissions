class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = len(heights) -1
        l = 0
        answer = 0
        
        while l < r:
            answer = max(answer,((r-l)*min(heights[l],heights[r])))
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1

        return answer