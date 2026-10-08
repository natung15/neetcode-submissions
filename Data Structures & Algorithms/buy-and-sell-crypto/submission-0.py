class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 101
        record = 0
        for x in prices:
            low = min(x,low)
            record = max(record, x - low)
        return record