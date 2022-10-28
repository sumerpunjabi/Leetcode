class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        record = {}
        
        for i, x in enumerate(nums):
            difference = target - x
            if difference in record:
                return (record[difference], i)
            else:
                record[x] = i