class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        i=0
        answer = []
        while i < len(sortedNums):
            if i > 0 and sortedNums[i] == sortedNums[i - 1]: # this prevents duplicate answers ie [0,0,0,0]
                i += 1
                continue
            l=i+1
            r=len(sortedNums) -1
            while l < r:
                test = sortedNums[i]+sortedNums[l]+sortedNums[r]
                if test == 0:
                    answer.append([sortedNums[i], sortedNums[l], sortedNums[r]])
                    l+=1
                    r-=1
                    while l < r and sortedNums[l] == sortedNums[l-1]: 
                        #this increments l incase there are duplocates after finding the answer but also prevents infinite loops
                        l+=1
                else:
                    if test < 0:
                        l+=1
                    else:
                        r-=1
            i+=1
        return answer
                
