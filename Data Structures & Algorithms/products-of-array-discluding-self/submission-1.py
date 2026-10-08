class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length

        left = 1
        for x in range(length):
            answer[x] = left
            left *= nums[x]

        right = 1
        for x in reversed(range(length)):
            answer[x] *= right
            right *= nums[x]
        return answer