class Solution:
    
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        
        for i in range(0, n):
            if nums[i] != nums[count]:
                count += 1
                nums[count] = nums[i]
        
        return count + 1
