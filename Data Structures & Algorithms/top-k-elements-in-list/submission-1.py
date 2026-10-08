class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for x in nums:
            dict[x] = dict.get(x,0) + 1
        
        buckets = [[]for x in range(len(nums)+1)]

        for n,c in dict.items():
            buckets[c].append(n)

        answer= []

        for bucket in reversed(buckets):
            for x in bucket:
                answer.append(x)
                if len(answer) == k:
                    return answer
        return answer
