class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the count for each number in the list +=1
        dict = {}
        for x in nums:
            dict[x] = dict.get(x,0) +1
        
        
        # this creates an empty list for each list enumeration for the amount of values there are
        buckets = [[] for x in range(len(nums)+1)]
  

        #this gathers the count for each item from the dict and adds it to the bucket n is the number that has appeared c is the count
        for n,c in dict.items():
            buckets[c].append(n)
        #create the list to return
        answer = []
        #iterating backwards from the top of the range
        for bucket in reversed(buckets):
            for values in bucket:
                answer.append(values)
                if len(answer) == k:
                    return answer