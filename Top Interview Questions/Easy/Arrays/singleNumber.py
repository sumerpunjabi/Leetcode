class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        s = set()

        for i in nums:
            if i in s:
                s.remove(i)
            else:
                s.add(i)

        return s.pop()