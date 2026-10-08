class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) #[ -4,-1,-1,0,1,2 ]
        answer= []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                test = nums[l] + nums[i] + nums[r]
                if test < 0:
                    l+=1
                elif test > 0:
                    r-=1
                else: 
                    answer.append([nums[l], nums[i], nums[r]])
                    l+=1
                    while  l < r and nums[l] == nums[l-1]:
                        l+=1
        return answer
        
        

            
                

        