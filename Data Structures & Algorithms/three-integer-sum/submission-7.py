class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums) #[ -4,-1,-1,0,1,2 ]
        answer= []
        for i in range(len(sortedNums)):
            
            l = i+1
            r = len(sortedNums)-1
            
            while l < r:
                test = sortedNums[l] + sortedNums[i] + sortedNums[r]
                if test == 0:
                    if [sortedNums[l], sortedNums[i], sortedNums[r]] not in answer:
                        answer.append([sortedNums[l], sortedNums[i], sortedNums[r]])
                    l+=1
                    r-=1
                    while (sortedNums[l] == sortedNums[l-1] or sortedNums[r] == sortedNums[r+1]) and l < r:
                        if sortedNums[l] == sortedNums[l-1]:
                            l+=1
                        if sortedNums[r] == sortedNums[r+1]:
                            r-=1 
                else:
                    if test < 0:
                        l+=1
                    else:
                        r-=1
        return answer
        
        

            
                

        