class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums) #[ -4,-1,-1,0,1,2 ]
        answer= []
        for i in range(len(sortedNums)):
            if i > 0 and sortedNums[i] == sortedNums[i-1]:
                continue
            l = i+1
            r = len(sortedNums)-1
            while l < r:
                test = sortedNums[l] + sortedNums[i] + sortedNums[r]
                if test < 0:
                    l+=1
                elif test > 0:
                    r-=1
                else: 
                    answer.append([sortedNums[l], sortedNums[i], sortedNums[r]])
                    l+=1
                    while  l < r and sortedNums[l] == sortedNums[l-1]:
                        l+=1
        return answer
        
        

            
                

        